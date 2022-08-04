import sys
import os
import shlex

from modules.Commands import run_command, InputCommand, close

from .color_text import Colortext
from .ascii import ASCII


def run():
    """
    Run the CLI.
    """
    console_clear()
    display_title()
    try:
        while True:
            command, *arguments = shlex.split(input(">> "))
            run_command(InputCommand(command, arguments))
    except KeyboardInterrupt:
        print()
        close()


def console_clear() -> None:
    platform = sys.platform
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def display_title():
    print(Colortext(ASCII.foxploit_title_with_face).orange())
    print(Colortext('FoXploit CLI').bold().green())
    print(Colortext('Version: ').bold() + '0.1.0')
    print(Colortext('Author: ').bold() + 'Yoann "Fxxx" Renard')
    print(Colortext('License: ').bold() + 'MIT')
    print(Colortext('Github: ').bold() + 'https://github.com/Yoann-Renard/FoXploit' + '\n')

