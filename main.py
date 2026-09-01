# Copy this into your editor!

def calculate_discounted_cost(number_of_coffees):
    total = number_of_coffees * 3

    if number_of_coffees >= 5:
        total -= 2
        return total
    return total
    # 2. Check if number_of_coffees is 5 or greater
    # 3. If it is, subtract 2 from the total
    # 4. Return the final total
    
    pass # <-- Delete this word and write your code!

# --- Test cases ---
# When you run your code, these should print the correct numbers!
print(calculate_discounted_cost(3)) # Should print 9
print(calculate_discounted_cost(5)) # Should print 13 
print(calculate_discounted_cost(10)) # Should print 28