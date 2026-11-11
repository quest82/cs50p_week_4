import random

def main():
    print(get_level())


def get_level():
    while True:
        level = int(input("Level: "))
        if level in range(1, 4):
            return level


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()