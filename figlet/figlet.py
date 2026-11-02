import sys
import pyfiglet

def main():
    result = None
    if len(sys.argv) == 1:
        text = input("Input: ")
        result = pyfiglet.figlet_format(text)
    elif (sys.argv[1] == '-f' ) or (sys.argv[1] == '--font' ):
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            text = input()
            result = pyfiglet.figlet_format(text, font=sys.argv[2].strip())
        else:
            sys.exit('Wrong font name')

    else:
        sys.exit('Wrong option')
    
    return result
 

# print(pyfiglet.figlet_format('Fun'))

print(main())
