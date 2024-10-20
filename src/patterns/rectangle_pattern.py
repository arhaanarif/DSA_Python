def rectangle_pattern(n,m):
    pattern=[]
    for _ in range(n):
        pattern.append('*'*m)
    return pattern

n=int(input('Enter number of rows: '))
m=int(input('Enter number of columns: '))
pattern=rectangle_pattern(n,m)
print(pattern)