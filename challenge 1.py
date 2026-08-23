#challenge 1
# i dont understand this yet

def is_balanced(s):
    stack = [] 
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in s: 
        # 1. Is it an open bracket?
        if char in ['(', '{', '[']:
            stack.append(char)
            
        # 2. Is it a close bracket?
        elif char in matching_brackets:
            # Make sure the stack isn't empty before we try to pop!
            if len(stack) == 0:
                return False
                
            top_item = stack.pop()
            
            # Use square brackets [] to look up the match in the dictionary
            if top_item != matching_brackets[char]:
                return False
                
    # 3. Did we finish with an empty stack?
    if len(stack) == 0:
        return True
    else:
        return False