





def isValid(s):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack=[]
    for char in s:
        if(char in '({['):
            stack.append(char)
        elif char in ')}]':
            if(not stack or stack[-1] != pairs[char]):
                return False
            stack.pop()
    return len(stack) ==0

     

# Test
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))       # False





