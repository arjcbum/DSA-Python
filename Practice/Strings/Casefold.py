# using in-built method

txt = "Hello Abhishek, And Welcome To This World!"
print("casefold(): " + txt.casefold())


# using manual way
# way1

txt = "Hello Abhishek, And Welcome To This World!"
if txt:
    s = ""
    for i in txt:
        s += i.lower()
    print("manual,way1: " + s)


# way2

txt = "Hello Abhishek, And Welcome To This World!"
if txt:
    s = ""
    for i in txt:
        if (i >= "A") and (i <= "Z"):
            s += chr(ord(i) + 32)
        else:
            s += i
    print("manual,way2: " + s)
