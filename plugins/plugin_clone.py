import os
import subprocess
import sys

from loguru import logger

from plugins.base import Command
from utils.parser import create_parser


class Clone(Command):

    def execute(self) -> None:
        parser = create_parser()
        args = parser.parse_args()

        if not args.repository:
            create_parser().print_help()
            sys.exit(0)

        if not os.path.exists('sandbox'):
            os.makedirs('sandbox')

        logger.info("Downloading repository")

        subprocess.Popen(cwd='./sandbox',
                         args=['git', 'clone', args.repository],
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.DEVNULL).communicate()

        logger.info("Done")
