from random import randint

def main():
    while True:
        level = input("Level: ")

        if level.isdigit():
            if int(level) > 0:
                print(game(int(level)))
                break

def game(val):
    secret_num = randint(1, val)
    while True:
        guess = input("Guess: ")
        
        if guess.isdigit() and int(guess) > 0:
            if int(guess) == secret_num:
                return 'Just right!'
            elif int(guess) < secret_num:
                print("Too small!")
            elif int(guess) > secret_num:
                print("Too large!")
         



main()   