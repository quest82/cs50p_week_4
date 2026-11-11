import random

def main():
    level = get_level()

    print(generate_integer(level))


def get_level():
    while True:
        level = int(input("Level: "))
        if level in range(1, 4):
            return level


def generate_integer(level):
    if level not in range(1, 4):
        raise ValueError

    try:
        if level == 1:
            integer = random.randrange(10)
        if level == 2:
            integer = random.randrange(10, 100)
        if level == 3:
            integer = random.randrange(100, 1000)
    except ValueError:
        print('Wrong input')
    else:
        return integer

main()

if __name__ == "__main__":
    main()