def count_consonants(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in string:
        if letter not in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowels_count=count_consonants(string)
print(f"Number of consonants in the string are {vowels_count}")