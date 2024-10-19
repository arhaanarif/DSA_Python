def inverted_pyramid(n):
    for i in range(n,0,-1):
        stars='*'*(2*i-1)
        spaces=' '*(n-i)
        print(spaces+stars+spaces)


inverted_pyramid(10)