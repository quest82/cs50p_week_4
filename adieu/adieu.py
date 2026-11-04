def main():
    names = []
    while True:
        try:
            name = input('Name: ').lower()
        except EOFError:
            print()
            break
        else:
            names.append(name.capitalize().strip())
    print(adieu(names))

def adieu(x):
    import inflect
    p = inflect.engine()
    result =  p.join(x)

    return f"Adieu, adieu, to {result}"



main()