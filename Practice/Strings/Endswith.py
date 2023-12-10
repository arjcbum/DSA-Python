# using in-built method

txt = "My name is Abhishek Raj."
print("endswith(): ", txt.endswith("Raj."))

# manually
# way1

txt = "My name is Abhishek Raj."
endStr = "Raj."
x = False
if txt and len(endStr) <= len(txt):
    txtArr = txt.split(" ")
    if endStr == txtArr[-1]:
        x = True
    else:
        x = False
print("way1: ", x)

# way2

txt = "My name is Abhishek Raj."
endStr = "Raj."
if txt and len(txt) >= len(endStr):
    x = len(txt) - len(endStr)
    y = 0
    while x != len(txt) and endStr[y] == txt[x]:
        x += 1
        y += 1
    if x == len(txt):
        q = True
    else:
        q = False
    print("way2: ", q)
