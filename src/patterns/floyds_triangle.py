def floyds_triangle(n):
    num=1
    for i in range(n):
        row=[]
        for j in range(i):
            row.append(str(num))
            num+=1
        print(' '.join(row))

floyds_triangle(5)
