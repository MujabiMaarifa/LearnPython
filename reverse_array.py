def printArray(arr) :
    for x in arr :
        print(x, end = "")
    print()
def reverseArray(arr) :
    arr.reverse()

arr1 = [1,2,3,4,5,6]
print("Your array is : ")
printArray(arr1)

reverseArray(arr1)
print("Reversed array: ")
printArray(arr1)
