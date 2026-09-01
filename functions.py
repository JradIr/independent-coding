def get_name(name):
    return name

def is_long_word(check):
    if len(check) > 5:
        return True
    else:
        return False

name = get_name("raven")

check = is_long_word("qwerty")
print(check)
print(name)