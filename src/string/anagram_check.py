def is_anagram(str1: str, str2: str):
    return sorted(str1) == sorted(str2)

str1 = input("Enter a string1: ")
str2 = input("Enter a string2: ")
print(is_anagram(str1, str2))
