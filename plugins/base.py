from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class Invoker:

    _on_command = None

    def set_on_command(self, command: Command):
        self._on_command = command

    def invoke_command(self) -> None:

        if isinstance(self._on_command, Command):
            self._on_command.execute()
