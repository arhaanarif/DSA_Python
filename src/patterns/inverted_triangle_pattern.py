def triangle_pattern(n):
    pattern=[]
    for i in range(n,0,-1):
        pattern.append('*'*i)

    return pattern

n=int(input('Enter n: '))
print(triangle_pattern(n))