"""
example
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
a. count in 10s from 0 to 100
"""
for i in range(0, 100, 10):
    print(i, end=' ')
print()

"""
b. count down from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
"""
n = int(input("Enter Number of Stars:"))
for i in range(0, n):
    print('*', end='')
print()

"""
d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1
"""
n = int(input("Enter Number of Stars:"))
m = (2*n)-2
for i in range(0, n):
    for j in range(0,m):
        print(end='')
    m = m-1
    for k in range(0, i + 1):
        print('*', end='')
    print()