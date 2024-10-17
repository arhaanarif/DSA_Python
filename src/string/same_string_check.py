def same_string(s,t):
    while len(s)==len(t):
        if t==s:
            return True
        else:
            return False
    return False
s=input("Enter string:")
t=input("Enter string:")
print(same_string(s,t))