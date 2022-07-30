from dataclasses import dataclass, field


@dataclass(frozen=True)
class Command:
    """Class that represents a command."""
    command: str
    arguments: list[str] = field(default_factory=list)


def run_command(command: Command) -> None:
    match command:
        case _:
            print(f"Unknown command {command}.")


commands = [
    Command("help", ["help"]),
    Command("clear", ["clear"]),
    Command("exit", ["exit"]),
    ]
