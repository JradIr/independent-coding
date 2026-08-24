#challenge 3 

def fizzbuzz(n):
    # 1. Start a 'for' loop to go from 1 up to n (inclusive)
    for num in range(1, n+1):
        
        # 2. Check if the number is divisible by BOTH 3 and 5 first!
        # Hint: use num % 3 == 0 and num % 5 == 0
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            
        # 3. Otherwise, check if it is divisible by just 3
        elif num % 3 == 0:
            print("Fizz")
            
        # 4. Otherwise, check if it is divisible by just 5
        elif num % 5 == 0:
            print("Buzz")
            
        # 5. If none of the above are true, just print the number itself
        else:
            print(num)

# Test the function by calling it with the number 15
fizzbuzz(15)
print("github repository")