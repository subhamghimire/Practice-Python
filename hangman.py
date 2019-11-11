import random
List = ['DOG', 'MONKEY', 'APPLE', 'HOUSE', 'DOOR', 'SPIDER', 'DOPE', 'PYTHON', 'MAGIC', 'NATURAL']
a = random.choice(List)
l = "_ " * len(a)
# print(a)
print(l)
user_input = input("Input a letter")
turn = 10
while turn > 0:
    failed = 0
    for character in a:
        if character in user_input:
            print(character)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        break
    another_input = input("Input next letter")
    user_input += another_input

    if user_input not in a:\
        turn -= 1
        if turn == 0:
            print("you loose")
