n = 5
# 1st method

for i in range(1, n+1):
    for j in range(1, n+1):
        if j > n-i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# 2nd method

aList = []
for i in range(1, n+1):
    aList.append(' '*(n-i) + '*'*i)
print('\n'.join(aList))