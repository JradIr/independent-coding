shelf = {"Apple" : 5, "Orange" : 4, "Banana" : 3}

def apply_discount(number):
    if number >= 15:
        number = number * 0.90
    return number

total_bill = 0

while True:
    print(f"Menu {shelf}")
    cart = input("What would you like to order? ")

    if cart not in shelf:
        print("Not on the shelf")
    else:
        total_bill += shelf[cart]
        print(f"Ordered {cart}, your bill is {total_bill}")

    program_end = input("type 'done' if you are finished, enter to keep shopping: ")
    if program_end.lower() == "done":
        break

print(total_bill)
