#challenge 2 done!

def count_vowels(word):
    # 1. Create a variable to keep track of the count, starting at 0
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    # 2. Start a 'for' loop to go through each character in 'word'
    for char in word:
        if char in vowel:
            count += 1
    return count
    
        # 3. Inside the loop, use an 'if' statement to check if the character is a vowel
        
            # 4. If it is a vowel, add 1 to your count variable
            
    # 5. After the loop finishes, return the final count

myWord = input("What is your word? ")
vowelCount = count_vowels(myWord)
print(vowelCount)