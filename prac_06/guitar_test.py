from guitar import Guitar

test_1 = Guitar(name='Gibson L-5 CES', year=1922, cost=16035.40)
test_2 = Guitar(name='Another Guitar', year=2007, cost=130)
print(test_1)
print(test_2)

print(Guitar.get_age(test_1))
print(Guitar.get_age(test_2))

print(Guitar.is_vintage(test_1))
print(Guitar.is_vintage(test_2))


