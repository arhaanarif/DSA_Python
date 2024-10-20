def right_aligned_triangle(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        print(spaces + stars)

right_aligned_triangle(5)
