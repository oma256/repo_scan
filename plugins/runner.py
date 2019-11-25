import subprocess
import os
import sys

from loguru import logger

from plugins.parser import create_parser


def run_git_clone_process() -> None:
    args = create_parser().parse_args()
    repository = args.repository

    logger.info("Downloading repository")

    if not repository:
        create_parser().print_help()
        sys.exit(0)

    if not os.path.exists('sandbox'):
        os.makedirs('sandbox')

    subprocess.Popen(cwd='./sandbox',
                     args=['git', 'clone', repository],
                     stderr=subprocess.STDOUT,
                     stdout=subprocess.DEVNULL).communicate()

    logger.info("Done")
