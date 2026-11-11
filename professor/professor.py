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
                prompt = None
            
            if prompt == answer:
                score += 1
                break
            if count == 3:
                print('EEE')
                print( f'{question[0]} + {question[1]} = {answer}')
                break
        
            print('EEE')
            count += 1

    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1,4):
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError



if __name__ == "__main__":
    print(main())