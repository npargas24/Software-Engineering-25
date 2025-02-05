stringyBoy = "I'm one stringy boy"
characterBoy = stringyBoy[0]

letterArray = []
reverseArray = []

for i in stringyBoy:
    letterArray.append(i)

for j in range(len(stringyBoy)):
    reverseArray.append(letterArray.pop())

for char in reverseArray:
    print(char, end='')
print()
    

