def is_substring(string, sub_string):
    return sub_string.lower() in string.lower()

string=input("enter string:")
sub_string=input("enter substring:")
print(is_substring(string, sub_string))