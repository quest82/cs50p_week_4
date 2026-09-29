import sys
import pyfiglet

def main():
    text = input()
    return figger(text)

def figger(str):
    return pyfiglet.figlet_format(str)

# print(pyfiglet.figlet_format('Fun'))

print(main())
