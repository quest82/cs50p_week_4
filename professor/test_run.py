import builtins
import random
import professor

numbers = iter([6,6, 0,4, 8,7, 1,2, 3,3, 4,4, 5,5, 2,2, 9,0, 7,1])
replies = iter(["1",
                "12", "4", "15",
                "0", "0", "0",        # problem 4 wrong three times
                "6", "8", "10", "4", "9", "8"])

random.randint = lambda a, b: next(numbers)

def fake_input(prompt=""):
    reply = next(replies)
    print(prompt + reply)
    return reply

builtins.input = fake_input
print(professor.main())