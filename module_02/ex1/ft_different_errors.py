"""Handling Different Types of Errors and catching multiple errors together"""


def garden_operations():
    try:
        print("\nTesting ValueError...")
        print(int("hello"))
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\nTesting KeyError...")
        plants = {"appel": 10, "orange": 5}
        print(plants["missing\\_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    try:
        print("\nTesting multiple errors together...")
        print(int("abc"))
        9 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


"""Runs all error demonstrations."""


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
