import sys
import os

from modules.CLI import Colortext


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
    print(Colortext(ASCII.fox_side).orange() + '\n')


