N = int(input())
i=0
# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
while i<N:
    sumArray[i]=(numArray1[i]+numArray2[i])
    i+=1


# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")
