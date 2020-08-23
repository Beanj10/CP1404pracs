# setting initial parameters
n = int(input("Number of items:"))
total=0

# error checking
while n < 0:
    print('Invalid number of items!')
    n = int(input("Number of items:"))

# loop entries and calculate total
for i in range(0, n):
    price = float(input("Price of item:"))
    total = total+price
if total > 100:
    total = round(total - total * 0.1, 2)
print('Total price for {} items is ${}'.format(n, total))