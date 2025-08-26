def error_print():
    inputs = int(input())
    values = []
    for i in range(inputs):
        values.append(input())
    for j in values:
        l1 = j.split(" ")
        try:
            print(int(l1[0])//int(l1[1]))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(l1[1]))
error_print()
