n = 5

for i in range(1, n+1):
    print(' ' * (n-i) + '* ' * i)


# another pat
c = 65
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= n-i:
            print(' ', end='')
        else:
            print(f'{chr(c)} ', end='')
            c += 1
    c = 65
    print()
