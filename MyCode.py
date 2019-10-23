
numbers = [11, 22, 33, 40, 55, 115, 20]

for number in numbers:
    if number % 2 == 0 and number % 3 == 0:
        print(number)
        break
else:
    print("Not found")