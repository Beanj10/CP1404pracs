
import random

picks = int(input('How many quick picks? '))
list = [[0 for i in range(6)] for j in range(picks)]

for i in range(picks):
    for j in range(6):
        number = random.randint(1, 45)
        while number in list[i]:
            number = random.randint(1, 45)
        else:
            list[i][j] = number
    list[:][i].sort()

for k in range(picks):
    for l in range(6):
        print(str(list[k][l]).zfill(2), end=" ")
    print('\n', end="")

