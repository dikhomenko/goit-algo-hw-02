def check_brackets(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"

# Тестування функції
test_expressions = [
    ("( ){[ 1 ]( 1 + 3 )( ){ }}", "Симетрично"),
    ("( 23 ( 2 - 3);", "Несиметрично"),
    ("( 11 }", "Несиметрично")
]

for expr, expected in test_expressions:
    result = check_brackets(expr)
    print(f"{expr}: {result} (очікувано: {expected})")
