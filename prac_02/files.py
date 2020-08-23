#Question 1
name = input('Please enter your name: ')

file_name = open('name.txt', 'w')
file_name.write(name + '\n')

#Question 2
file_name = open('name.txt', 'r')
fname = file_name.readline(1)
print('Your name is', name)

#Question 3
file_name = open('numbers.txt', 'w')
file_name.write('17\n42\n400\n')
file_name.close()
file_name = open('numbers.txt', 'r')
line1 = [int(i) for i in file_name.readlines(1)]
line2 = [int(i) for i in file_name.readlines(2)]

sm = sum(line1 + line2)
print('Sum = ', sm)

#Question 4
file_name = open('numbers.txt', 'r')

number = [int(i) for i in file_name.readlines()]
sm = str(sum(number))
file_name = open('numbers.txt', 'a')
file_name.write('\ntotal = ' + sm)