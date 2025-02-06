import random
Array=[]
sumArr = []
Range = random.randint(0,10)
N = 100
for i in range (0,N):
    Array.append(random.randint(0,N))

SegNum = int(len(Array)/Range)

for i in range(SegNum):
    sum = 0
    for j in range(i, i+Range):
        sum = sum + Array[j]
    sumArr.append(sum)

remainder = len(Array)%SegNum

print("this is the sum array: ", sumArr)
print("This is how many elements didn't fit: ", remainder)
