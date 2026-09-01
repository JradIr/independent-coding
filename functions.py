"""def get_name(name):
    return name

def is_long_word(check):
    if len(check) > 5:
        return True
    else:
        return False

name = get_name("raven")

check = is_long_word("qwerty")
print(check)
print(name)"""

#more parameters

def greet(name, greeting="hello"):
    return f"{greeting}, {name}"

print(greet("raven", "Hi"))
print(greet("lianne"))

def introduce(greet, name, age, title="Mr/Mrs"):
    return f"{greet} {title} {name}, you are {age} years old."

result = introduce("Hello", "raven", "20")
print(result)