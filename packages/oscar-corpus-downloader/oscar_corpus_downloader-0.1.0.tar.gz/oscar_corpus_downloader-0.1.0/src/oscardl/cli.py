import logging
import os.path
import sys
import time
from datetime import datetime, timedelta

import click
from loguru import logger

from oscardl.download import download_corpus


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        logger.info(
            "Process started on {}".format(start_time.strftime("%Y/%m/%d %H:%M:%S"))
        )
        func(*args, **kwargs, timestamp=start_time.strftime("%Y%m%d-%H%M%S"))

        end_time = datetime.now()
        logger.info(
            "Process ended on {}".format(end_time.strftime("%Y/%m/%d %H:%M:%S"))
        )

        logger.info(
            "Elapsed Time: {}".format(
                timedelta(
                    seconds=round(
                        time.mktime(end_time.timetuple())
                        - time.mktime(start_time.timetuple())
                    )
                )
            )
        )

    return wrapper


@click.group()
@click.option("--debug", is_flag=True)
def cli(debug):
    log = logging.getLogger("")
    log.handlers = []
    log_format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    # Adding a stdout handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(log_format)
    log.addHandler(ch)


@time_decorator
@cli.command("download")
@click.option("-u", "--url", help="OSCAR corpus url", required=True, type=str)
@click.option("-o", "--output-dir", help="Output directory", required=True, type=str)
@click.option("--resume", help="Resume download", is_flag=True, type=bool)
def command_download(
    url: str = None,
    output_dir: str = None,
    timestamp: str = None,
    resume: bool = False,
):
    username = os.environ.get("OSCAR_USERNAME")
    password = os.environ.get("OSCAR_PASSWORD")

    if os.path.isdir(output_dir):
        click.confirm(
            "The output directory already exists. Do you want to resume download ?",
            abort=True,
        )

        click.echo("Resuming download")

    if not os.path.isdir(output_dir):
        logger.info("Creating directory")
        os.makedirs(output_dir)

    download_corpus(
        url=url,
        output_dir=output_dir,
        timestamp=timestamp,
        username=username,
        password=password,
    )


if __name__ == "__main__":
    cli()
