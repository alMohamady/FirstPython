
for i in range(1, 200):

    if i % 5 == 0:
       pass
    else:
       print(i)

print("Hello world")
#===================================================

for i in range(1, 200):

    if i % 5 != 0:
        continue

    print(i)

print("Hello world")

#===================================================

x = int(input("How Many Boxes in the inventory: "))
a = 20

i = 1
while i <= x:

    if i > a:
        print("Error: Out of Stock")
        break

    print("Box Num " + str(i))
    i += 1

print("Hello World")