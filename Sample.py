def sample(num):
    if num >= 18:
        print("you are an adult")
    else:
        print(" you are a child")
    print(num)

number = sample("19")

name = input("")
print(name)

#next is add a switch case code block
choice = input("Name a fruit: ")
match choice:
    case "mango":
        print("you chose mango")
    case "banana":
        print("you chose banana")
    case "apple":
        print("you chose apple")
    case _:
        print("you didn't name a fruit...")
print(f"your choice is {choice}, and your age is {number}")

