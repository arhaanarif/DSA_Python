def is_palindrome(string):
    cleaned_string="".join(char.lower() for char in string if char.isalnum())
    return cleaned_string==cleaned_string[::-1]

string=input("enter the string:")
print(is_palindrome(string))