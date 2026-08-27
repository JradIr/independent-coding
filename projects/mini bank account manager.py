def get_valid_amount(params):
    while True:
        amount = int(input(params))
        if amount > 0:
            return amount

name = input("What is your name: ")
current_balance = 100
withdraw_list = []
deposit_list = []

while True:
    print("1 - withdraw\n2 - deposit\n3 - exit")
    choice = int(input(":"))
    if choice == 1:
        while True:
            withdraw = get_valid_amount("Input amount: ")
            if withdraw > current_balance:
                print("You are going below zero")
            else:
                withdraw_list.append(withdraw)
                current_balance -= withdraw

            stop_condition = input("withdraw again? y/n")
            if stop_condition == "n":
                break
    elif choice == 2:
        while True:
            deposit = get_valid_amount("Input amount: ")
            deposit_list.append(deposit)
            current_balance += deposit

            stop_condition = input("Deposit again? y/n")
            if stop_condition == "n":
                break
    elif choice == 3:
        print("thank you for banking with us!")
        break

print(withdraw_list)
print(deposit_list)
print(name, "Your current balance is",current_balance)
print("bakit hindi siya nag update?")