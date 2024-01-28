n = 5
# 1st method

for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end = "")
    print("")


# 2nd method

aList = []
for i in range(1, n+1):
    aList.append('* ' * i)
print('\n'.join(aList))


# Another Pat

for i in range(0, n):
    for j in range(0, i+1):
        print(f'{j+1} ', end = "")
    print("")

# Another Pat
c = 1
for i in range(0, n):
    for j in range(0, i+1):
        print(f'{c} ', end = "")
        c += 1
    print("")

# Another Pat
for i in range(0, n):
    for j in range(0, i+1):
        print(f'{chr(j+65)} ', end = "")
    print("")


c = 65
for i in range(0, n):
    for j in range(0, i+1):
        print(f'{chr(c)} ', end = "")
        c += 1
    print("")
