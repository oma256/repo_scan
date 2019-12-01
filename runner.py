from plugins.base import Invoker
from plugins.plugin_clone import Clone
from plugins.plugin_flake8 import Flake8

COMMANDS = [
    Clone(),
    Flake8(),
]


def execute_scanner():
    for command in COMMANDS:
        invoker = Invoker()
        invoker.set_on_command(command)
        invoker.invoke_command()
