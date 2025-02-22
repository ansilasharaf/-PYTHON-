#Write a program to reverse a string and check if it is a palindrome.



# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to check if a string is a palindrome
def is_palindrome(s):
    reversed_s = reverse_string(s)
    return s == reversed_s

# Input from user
input_string = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

# Check if it's a palindrome
if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
