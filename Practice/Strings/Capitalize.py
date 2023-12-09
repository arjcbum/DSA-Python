# in-built method

txt = "my name is Abhishek. how can I help you?"
print(txt.capitalize())

# manually
# way1
txt = "my name is Abhishek. how can I help you?"
if txt:
    strTxt = txt[0].upper() + txt[1:]
    print(strTxt)

# way2
txt = "my name is Abhishek. how can I help you?"
if txt:
    if (ord(txt[0]) >= 97) and (ord(txt[0]) <= 122):
        txt = chr(ord(txt[0]) - 32) + txt[1:]
    print(txt)

# way3 - capitalize all the letters after '.'
txt = "my name is Abhishek. how can I help you?"
if txt:
    s = ""
    for i in range(len(txt)):
        if (txt[i-2] == "." and txt[i-1] == " ") or (txt[i-1] == "." and txt[i] != " "):
            s += txt[i].upper()
        else:
            s += txt[i]
    print(s[0].upper()+s[1:])
