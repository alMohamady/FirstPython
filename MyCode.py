
a = 10
b = 2

try:
    print("connection Open")
    print(a / b)
    num = int(input("Enter the number"))
    print(num)
except ZeroDivisionError as ex:
    print("div on 0 not allowed", ex)
except ValueError as ex:
    print("Invalid Input", ex)
except Exception as ex:
    print("General Error")
finally:
    print("connection Close")

print("Hello")
