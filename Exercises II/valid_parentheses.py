

def valid_parentheses(str):
    if str.count('(') == str.count(')') and str[0] == '(' and str[-1] == ')':
        return True
    return False




print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False