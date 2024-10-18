def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0  # i for string s, j for string t

    # Loop through s and check for matching characters in t
    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match, move j to the next character in t
            j += 1
        i += 1  # Always move i to the next character in s

    # If j has traversed all characters in t, it's a subsequence
    return j == len(t)

# Example usage
s = input("Enter a string1: ")
t = input("Enter a string2: ")
print(is_subsequence(s, t))  # Output: True