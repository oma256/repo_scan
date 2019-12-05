from loguru import logger

from plugins.base import Command


class Flake8(Command):

    def execute(self) -> None:
        logger.info('Flake8 command')
