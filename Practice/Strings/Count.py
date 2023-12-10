# using in built method

txt = "I love apples, apples are my favorite fruit"
x = txt.count("apples")
print("count(): ", x)

# manually

# way1

txt = "I love apples, apples are my favorite fruit"
subStr = "apples"
count = 0
txtArr = txt.replace(",", " ").split(" ")
for i in txtArr:
    if subStr == i:
        count += 1
print("way1: ", count)

# way2

txt = "I love apples, apples are my favorite fruit"
subStr = "apples"
count = 0
i = 0
while i < len(txt):
    j = 0
    while j != len(subStr) and subStr[j] == txt[i]:
        j += 1
        i += 1
    if j == len(subStr):
        count += 1
    i += 1
print("way2: ", count)

