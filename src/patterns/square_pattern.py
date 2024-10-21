def generate_square(size):
    pattern=[]
    for _ in range(size):
        pattern.append('*'*n)
    return pattern

n=int(input("Enter size of square:"))
pattern=generate_square(n)
print(pattern)
