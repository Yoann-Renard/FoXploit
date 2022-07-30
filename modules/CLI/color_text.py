class Colortext:
    """
    Returns a colored text object.
    """
    def __init__(self, text: str) -> None:
        self.text = text
        self.ending = '\033[0m'

    def __str__(self) -> str:
        return self.text

    def __add__(self, text: str) -> 'Colortext':
        return Colortext(self.text + text)

    def bold(self) -> 'Colortext':
        self.text = '\033[1m' + self.text + self.ending
        return self

    def green(self) -> 'Colortext':
        self.text = '\033[92m' + self.text + self.ending
        return self

    def orange(self) -> 'Colortext':
        self.text = '\033[93m' + self.text + self.ending
        return self

    def red(self) -> 'Colortext':
        self.text = '\033[91m' + self.text + self.ending
        return self

    def blue(self) -> 'Colortext':
        self.text = '\033[94m' + self.text + self.ending
        return self