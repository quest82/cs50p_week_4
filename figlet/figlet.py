import sys
import pyfiglet

def main():
    text = input()
    return figger(text)

def figger(str):

    if len(sys.argv) == 1:
        return pyfiglet.figlet_format(str)

    elif (sys.argv[1] == '-f' ) or (sys.argv[1] == '--font' ):
        try:
            result = pyfiglet.figlet_format(str, font=sys.argv[2].strip())
        except pyfiglet.FontNotFound:
            sys.exit('Wrong font name')
        return result
    
    else:
        sys.exit('Wrong option')
       

# print(pyfiglet.figlet_format('Fun'))

print(main())
