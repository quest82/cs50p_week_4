import sys

def main():
    try:
        amount = sys.argv[1]
        if not amount.isdigit():
            raise ValueError
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Command-line argument is not a number")

main()