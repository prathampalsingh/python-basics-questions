n = int(input("eneter the number of elements to be entered: "))
arr= []
for x in range(n):
    num = int(input("enter the elements: "))
    arr.append(num)
    
print("before sorting: ",arr)
arr.sort()
print("after sorting: ",arr)

second_element = arr[1]
print("second smallest element: ",second_element)

second_last_element = arr[-2]
print("second last element: ", second_last_element)

arr.pop(0)
arr.insert(0,1)
#DOES THE SAME STUFF!!!


print(arr)

