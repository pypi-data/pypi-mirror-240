# OSCAR Corpus Downloader

Simple tool to download the OSCAR corpus.

## 1. Installation

Installation can be done using [pypi](https://pypi.org/project/oscar-corpus-downloader/):

```shell
$ pip install oscar-corpus-downloader
```

## 2. Usage

Submit an OSCAR access request following the procedure described on the [project page](https://oscar-project.org/).

Once you have received your credentials, you can use the command line interface to download an OSCAR corpus part.

```shell
$ export OSCAR_USERNAME=username
$ export OSCAR_PASSWORD=password
$ oscar download --help
Usage: oscar download [OPTIONS]

Options:
  -u, --url TEXT         OSCAR corpus url  [required]
  -o, --output-dir TEXT  Output directory  [required]
  --resume               Resume download
  --help                 Show this message and exit.

$ oscar download \
  --url https://oscar-prive.huma-num.fr/2301/fr_meta \
  -o ./oscar-fr
```

