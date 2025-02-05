def compareArr(arrayOne, arrayTwo):
    length = len(arrayOne)
    arrayOne.sort()
    arrayTwo.sort()
    arrayThree = []
    
    for i in range(length):
        if arrayOne[i] == arrayTwo[i]:
            print("they match!")
            arrayThree.append(arrayOne[i])
            print(arrayThree)

        else:
            print("no match")


array1 = [1, 2, 4, 3, 23, 85]
array2 = [1, 2, 3, 4, 76, 154]
compareArr(array1,array2)
        
