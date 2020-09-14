import statistics


def main():

    numbers = []

    for i in range(1, 6):
        number = float(input('Enter Number {:.0f}: '.format(i)))
        numbers.append(number)

    print('The first number is {:.0f}'.format(numbers[0]))
    print('The last number is {:.0f}'.format(numbers[-1]))
    print('The smallest number is {:.0f}'.format(min(numbers)))
    print('The largest number is {:.0f}'.format(max(numbers)))
    print('The average of the numbers is {:.2f}'.format(statistics.mean(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    users_name = input('Please enter your username:')

    access = users_name == usernames

    if access:
        print('Access granted')
    else:
        print('Access denied')


main()
