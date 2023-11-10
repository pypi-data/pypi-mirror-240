import json
import os
import re
from enum import Enum
from hashlib import sha256
from io import StringIO

import requests
from bs4 import BeautifulSoup
from loguru import logger
from tqdm import tqdm


class Status(str, Enum):
    EXISTS = "EXISTS"
    DOWNLOAD_SUCCESS = "DOWNLOAD_SUCCESS"
    DOWNLOAD_FAILED = "DOWNLOAD_FAILED"
    VALIDATION_FAILED = "VALIDATION_FAILED"


def get_unique_file_locations(
    url: str = None, response_content: bytes = None
) -> list[str]:
    """
    Extract corpus data file URLs

    Parameters
    ----------
    url: str
        Main webpage url (used to construct the full url)
    response_content: bytes
        Main webpage main content

    Returns
    -------
    List[str]
        List of data corpus files
    """

    soup = BeautifulSoup(response_content, "html.parser")
    return list(
        {
            "/".join([url, link["href"]])
            for link in soup.find_all("a", href=True)
            if re.match(r"^.*\.jsonl\.(gz|zst)$", link["href"])
        }
    )


def get_checksums_location(url: str = None, response_content: bytes = None) -> str:
    """
    Extract checksum URL from main webpage

    Parameters
    ----------
    url: str
        main webpage url (used to construct the full url)
    response_content: bytes
        main webpage main content

    Returns
    -------
    str
        checksum file URL
    """

    soup = BeautifulSoup(response_content, "html.parser")

    checksum_file = [
        "/".join([url, link["href"]])
        for link in soup.find_all("a", href=True)
        if "sha256" in link["href"]
    ][0]

    return checksum_file


def download_checksums(
    session: requests.sessions.Session = None,
    checksum_url: str = None,
    output_dir: str = None,
) -> dict:
    """
    Download checksum file from the oscar corpus page

    Parameters
    ----------
    session: requests.sessions.Session
        Opened requests session
    checksum_url: str
        Checksum file URL
    output_dir: str
        Directory where the file will be written

    Returns
    -------
    dict
        corpus file checksums
    """

    download = session.get(checksum_url)
    download.raise_for_status()

    checksum_file_basename = os.path.basename(checksum_url)
    checksum_file_target = os.path.join(output_dir, checksum_file_basename)

    with open(checksum_file_target, "w", encoding="UTF-8") as output_file:
        output_file.write(download.text)

    with StringIO(download.text) as buffer:
        lines = buffer.readlines()

        dictionary = {}

        for line in lines:
            (val, key) = line.strip("\n").split()
            dictionary[key] = val

        return dictionary


def validate_file(corpus_file: str = None, checksum: str = None):
    """
    Validate a file against its checksum

    Parameters
    ----------
    corpus_file: str
        Corpus file path
    checksum: str
        Corpus file checksum

    Returns
    -------
    bool
        True if the file is valid, False otherwise

    """

    hash_obj = sha256()

    with open(corpus_file, "rb") as input_file:
        while True:
            chunk = input_file.read(hash_obj.block_size)

            if not chunk:
                break

            hash_obj.update(chunk)

    return hash_obj.hexdigest() == checksum


def download_file(
    session: requests.sessions.Session = None,
    file_url: str = None,
    chunk_size: int = None,
    checksum: str = None,
    output_dir: str = None,
) -> Status:
    """
    Download a corpus file

    Parameters
    ----------
    session: requests.sessions.Session
        Opened request session
    file_url: str
        Corpus file URL
    chunk_size: int
        Download chunk size
    checksum: str
        Corpus file checksum
    output_dir: str
        Directory where the file will be written

    Returns
    -------
    oscar.download.Status
        File download status
    """

    output_file = os.path.join(output_dir, os.path.basename(file_url))

    if os.path.isfile(output_file):
        if validate_file(corpus_file=output_file, checksum=checksum):
            logger.info(
                f"{os.path.basename(file_url)} is already downloaded, skipping."
            )
            return Status.EXISTS

    download = session.get(file_url, stream=True)
    download.raise_for_status()

    if download.status_code != 200:
        return Status.DOWNLOAD_FAILED

    try:
        with open(output_file, "wb") as f:
            with tqdm(
                total=int(download.headers.get("content-length", 0)),
                desc=os.path.basename(output_file),
                miniters=1,
                unit_scale=True,
                unit_divisor=1024,
                unit="B",
            ) as progress_bar:
                for chunk in download.iter_content(chunk_size=chunk_size):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        progress_bar.update(len(chunk))
    except Exception:
        return Status.DOWNLOAD_FAILED

    if validate_file(corpus_file=output_file, checksum=checksum):
        return Status.DOWNLOAD_SUCCESS

    return Status.VALIDATION_FAILED


def download_corpus(
    url: str = None,
    output_dir: str = None,
    chunk_size: int = 4096,
    timestamp: str = None,
    username: str = None,
    password: str = None,
):
    """
    Download an oscar corpus part. It will check file hashes against those provided by huma-num

    Parameters
    ----------
    url: str
        The URL of the corpus part
    output_dir: str
        The directory where the downloaded corpus will be stored
    chunk_size: int
        Chunk size to apply during downloading
    timestamp: str
        Timestamp used to name the log file for the current download session
    username: str
        huma-num account username
    password: str
        human-num account password

    Returns
    -------
        None
    """

    with requests.session() as session:
        session.auth = (username, password)

        logger.info("Login in")
        response = session.get(url)

        if response.status_code != 200:
            raise Exception("Wrong login and/or password")

        logger.info("Fetching checksum file")

        checksums_url = get_checksums_location(
            url=url, response_content=response.content
        )

        checksums = download_checksums(
            session=session, checksum_url=checksums_url, output_dir=output_dir
        )

        results = {}

        logger.info("Extracting file list")
        to_be_downloaded = get_unique_file_locations(url, response.content)
        to_be_downloaded = sorted(to_be_downloaded)

        logger.info(f"Downloading {len(to_be_downloaded)} files")
        try:
            for data_url in to_be_downloaded:
                status = download_file(
                    session=session,
                    file_url=data_url,
                    chunk_size=chunk_size,
                    checksum=checksums[os.path.basename(data_url)],
                    output_dir=output_dir,
                )

                results[os.path.basename(data_url)] = status
        finally:
            logger.info("Dumping file status")
            with open(
                os.path.join(output_dir, f"status-{timestamp}.txt"), "w"
            ) as output_file:
                json.dump(results, output_file)
