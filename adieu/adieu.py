def main():
    names = []
    while True:
        try:
            name = input('Name: ')
        except EOFError:
            print()
            break
        else:
            names.append(name.capitalize().strip())
    print(names)

main()