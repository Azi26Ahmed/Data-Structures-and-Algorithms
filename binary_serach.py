def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
def intake():
    li=[]
    n=int(input("How manyb elements do u want to insert in the list"))
    for i in range(n):
        enter=int(input("Enter the element"))
        li.append(enter)
    return li
array=intake()
sorted_array=sorted(array)
key=int(input("Enter the key to be searched"))
ans=binary_search_recursive(sorted_array,key,0,len(sorted_array)-1)
if ans== -1:
    print("Key not found")
else:
    print(f"The key {key} is found at index {ans} in the sorted array")
    print("The sorted array is:",sorted_array)