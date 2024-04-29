from collections import deque

def is_palindrome(s):
    formatted_string = ''.join(char.lower() for char in s if char.isalnum())
    d = deque(formatted_string)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Тестування функції
test_strings = ["A man a plan a canal Panama", "No lemon, no melon", "Hello, World!", "Привіт, світе!", "1221", "02/02/2020", "level", "Madam, in Eden, I’m Adam"]
for test in test_strings:
    print(f"'{test}' -> {is_palindrome(test)}")
