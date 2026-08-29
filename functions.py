def get_greeting(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def greet(name):
    """Print a greeting for the given name."""
    print(get_greeting(name))


def is_valid_name(name):
    """Return True if the name is not empty."""
    return len(name.strip()) > 0


def get_formal_greeting(first_name, last_name=""):
    """Return a formal greeting. Last name is optional."""
    if last_name:
        return f"Good day, {first_name} {last_name}."
    return f"Good day, {first_name}."


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    greet("Raven")
    print(get_formal_greeting("Raven"))
    print(get_formal_greeting("Raven", "De La Rosa"))
    print("5 + 3 =", add_numbers(5, 3))

    name = input("Enter your name: ")
    if is_valid_name(name):
        print(get_greeting(name.strip()))
    else:
        print("Please enter a valid name.")
