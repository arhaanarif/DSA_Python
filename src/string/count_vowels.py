def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowels_count=count_vowels(string)
print(f"Number of vowels in the string are {vowels_count}")