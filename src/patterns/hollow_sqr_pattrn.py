def hollow_square_pattrn(n):
    pattern=[]
    if n==1:
        return ['*']
    if n==2:
        return['**','**']

    pattern.append('*'*n)

    for i in range(n-2):
        pattern.append('*' + ' ' * (n - 2) + '*')

    pattern.append('*' * n)
    return pattern

n=int(input('Enter n: '))
for row in hollow_square_pattrn(n):
    print(row)