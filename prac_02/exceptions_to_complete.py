finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an Integer: "))
        print("Valid result is:", result)
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)