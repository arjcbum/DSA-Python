# using in built method

txt = "banana"
strTxt = txt.center(20, "0")
print("center(): " + strTxt)

# manually
# way1

txt = "banana"
width = 20
filChar = "0"
halfInd = int((width - len(txt))/2)
strTxt = filChar*halfInd + txt + (width-len(txt)-halfInd)*filChar
print(strTxt)