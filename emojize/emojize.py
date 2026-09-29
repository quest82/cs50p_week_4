import emoji

def main():
    test = input()
    return emojis(test)

def emojis(str):
    return emoji.emojize(str, language='alias')

# print(emoji.emojize('Python is :smile_cat:', language='alias'))
# print(emoji.emojize('Python is :money_bag:'))
# print(emoji.emojize('Python is :thumbs_up:'))


print(main())