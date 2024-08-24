def password(n):
    for i in range(1, 20):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                print(i, j, end=' ')


password(6)
