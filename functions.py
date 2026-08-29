# Functions practice file
# A function is a reusable block of code that does one specific job.


def get_greeting(name):
    """Return a greeting message for the given name."""
    # return sends a value back to whoever called the function
    return f"Hello, {name}!"


def greet(name):
    """Print a greeting for the given name."""
    # This function calls get_greeting() and prints the result
    print(get_greeting(name))


def is_valid_name(name):
    """Return True if the name is not empty."""
    # strip() removes extra spaces from the start and end
    # len() counts characters — if length is 0, the name is empty
    return len(name.strip()) > 0


def get_formal_greeting(first_name, last_name=""):
    """Return a formal greeting. Last name is optional."""
    # last_name="" means last_name is optional when calling this function
    if last_name:
        return f"Good day, {first_name} {last_name}."
    # If no last name was given, use just the first name
    return f"Good day, {first_name}."


def add_numbers(a, b):
    """Return the sum of two numbers."""
    # a and b are parameters — values passed in when the function is called
    return a + b


def is_adult(age):
    """Return True if age is 18 or older, otherwise False."""
    # >= means "greater than or equal to"
    # This returns a boolean (True or False), not a printed message
    return age >= 18


# This block only runs when you execute this file directly (python functions.py)
# It will NOT run if another file imports functions.py
if __name__ == "__main__":
    greet("Raven")
    print(get_formal_greeting("Raven"))
    print(get_formal_greeting("Raven", "De La Rosa"))
    print("5 + 3 =", add_numbers(5, 3))

    # Test is_adult with different ages
    print("Age 16 is adult:", is_adult(16))
    print("Age 21 is adult:", is_adult(21))

    # Ask the user for their name and validate it before greeting
    name = input("Enter your name: ")
    if is_valid_name(name):
        print(get_greeting(name.strip()))
    else:
        print("Please enter a valid name.")
