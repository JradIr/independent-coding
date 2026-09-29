def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a child.")
    return age

def get_fruit_choice():
    choice = input("Name a fruit (mango, banana, or apple): ").strip().lower()
    
    match choice:
        case "mango":
            print("You chose mango.")
        case "banana":
            print("You chose banana.")
        case "apple":
            print("You chose apple.")
        case _:
            print("You didn't name a recognized fruit...")
            choice = "nothing"
            
    return choice

def main():
    name = input("What is your name? ").strip()
    print(f"Hello, {name}!")

    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number.")
            
    age = check_age(user_age)
    fruit = get_fruit_choice()

    print(f"\nSummary: Your name is {name}, your age is {age}, and your choice is {fruit}.")

if __name__ == "__main__":
    main()
print("done")
