"""Checks temperature input and handles invalid or extreme values."""


def check_temperature(temp_str):
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp_str = int(temp_str)
        if temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        elif temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return temp_str
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


"""Runs all test cases for temperature validation."""


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


test_temperature_input()
