"""Palindrome function."""


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def is_primo(number: int) -> bool:
    pass


def run() -> None:
    print(is_palindrome(1000))


if __name__ == "__main__":
    run()
