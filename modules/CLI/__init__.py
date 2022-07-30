import shlex

from .ascii import ASCII
from .color_text import Colortext
from .commands import *
from .utils import *


def run():
    """
    Run the CLI.
    """
    console_clear()
    display_title()
    while True:
        command, *arguments = shlex.split(input(">> "))
        run_command(Command(command, arguments))


