def check_num():
    try:
        num = int(input("Enter a number: "))
    except ValueError as err:
        raise Exception(err)
    else:
        print(f"Entered number: {num}")
    finally:
        print("Final block")


def file_error():
    try:
        name = str(input("Enter the file name: "))
        with open(name, 'r') as file:
            lines = file.read()
        print(lines)
    except FileNotFoundError as err:
        print(err)
    else:
        print(f"File name entered: {name}")


# check_num()

file_error()