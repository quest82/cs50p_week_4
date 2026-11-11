import random

def main():
    level = get_level()
    questions = []
    while len(questions) < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        questions.append((x, y))

    score = 0
    for question in questions:
        answer = question[0] + question[1]

        count = 1
        while True:
            try:
                prompt = int(input(f'{question[0]} + {question[1]} = '))
            except ValueError:
                pass
            if prompt == answer:
                score += 1
                break
            if count == 3:
                print( f'{question[0]} + {question[1]} = {answer}')
                break
        
            print('EEE')
            count += 1

    return score

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



if __name__ == "__main__":
    print(main())