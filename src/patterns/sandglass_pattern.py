def sandglass_pattern(n):
    for i in range(n,0,-1):
        stars='*'*(2*i-1)
        spaces=' '*(n-i)
        print(spaces+stars+spaces)

    for i in range(2,n+1):
        stars='*'*(2*i-1)
        spaces=' '*(n-i)
        print(spaces+stars+spaces)

sandglass_pattern(5)