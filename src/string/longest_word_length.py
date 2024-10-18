def longest_word_length(word):
    max_length = 0
    current_length = 0
    for letter in word:
        if letter != ' ':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    if current_length > max_length:
        max_length = current_length

    return max_length

word=input('Enter a string: ')
result = longest_word_length(word)
print(f"The longest word length is {result}")