import argparse
import sys

from loguru import logger


def get_repository_url():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository', dest='repository')

    args = parser.parse_args()
    repository = args.repository
    logger.info("Downloading repository")
    if not repository:
        parser.print_help()
        sys.exit(0)

    return repository

