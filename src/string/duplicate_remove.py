def remove_duplicates(s):

 # method-1
    seen=set()
    result=[]
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)


# method-2
    return ''.join(dict.fromkeys(s))

s=input("Enter string:")
print(remove_duplicates(s))