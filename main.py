# 1. Here is your Dictionary!
food_shelf = {"Coke": 4, "Sprite": 5, "Sandwich": 10} 

def apply_discount(current_total):
    # Check if they spent 15 or more
    if current_total >= 15:
        # Multiply by 0.90 to keep 90% of the price (a 10% discount)
        current_total = current_total * 0.90 
    return current_total

# 2. Set the starting total OUTSIDE the loop
total_bill = 0 

while True:
    print("Menu:", food_shelf)
    cart = input("Pick from the shelf: ")
    
    # 3. Check if the item is NOT in the dictionary keys
    if cart not in food_shelf:
        print("Sorry, we don't sell that!")
    else:
        # Look up the price in the dictionary and add it to the bill
        total_bill += food_shelf[cart] 
        print(f"Added {cart}. Current total is ${total_bill}")
    
    program_end = input("Type 'done' to pay, or press Enter to keep shopping: ")
    
    # 4. Use .lower() to catch "done", "Done", "DONE", etc.
    if program_end.lower() == "done":
        break

# 5. Apply the discount to the final amount after the loop finishes!
final_bill = apply_discount(total_bill)
print(f"Your final bill is: ${final_bill}")