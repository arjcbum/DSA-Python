# using in-built method

txt = "h\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))


# manually

# way1

txt = "h\te\tl\tl\to"
tabLength = 2
newGroup = " " * (tabLength-1)
txtStr = txt.replace("\t", newGroup)
print("way1: ", txtStr)


# way2

txt = "h\te\tl\tl\to"
txtArr = txt.split("\t")
tabLength = 4
newGroup = " " * (tabLength-1)
s = ""
newTxt = newGroup.join(txtArr)
print("way3: ", newTxt)