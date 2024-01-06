def selection_sort(myList):
    for i in range(len(myList) - 1):
        min_index = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j
        if i != min_index:
            temp = myList[i]
            myList[i] = myList[min_index]
            myList[min_index] = temp
    return myList


print(selection_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """

