from guitar import Guitar

guitars = [Guitar()]
i = 0
print("My guitars!")
name = input("Name:")
while name != '':
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    guitars.append(Guitar(name, year, cost))
    print("{} added.".format(guitars[i+1]))
    name = input("Name:")
    i = i + 1
print("These are my guitars:")


for j in range(1, len(guitars)):
    while Guitar.is_vintage(guitars[j]):
        vintage = "(vintage)"
    else:
        vintage = " "
    print("Guitar {} :{}".format(j, guitars[j]) + vintage)

