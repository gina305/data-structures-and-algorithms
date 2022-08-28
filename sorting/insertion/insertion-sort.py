def InsertionSort(arr=[8,4,23,42,16,15]):
    i=1

    for i in range(len(arr)):
        i=1
        j =  i - 1
        temp = arr[i]

        while j>=0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            print (f'{arr[j + 1]}= {arr[j]}')


            j = j - 1

        arr[j + 1] = temp
    print(arr)

InsertionSort()
# j = 0
# i = 1
# temp = 2nd value of array (4)
# arr[j] 1st value of array (8)
#
# while j is 0 or more and the 2nd value is less than the first value then
#     change the second value into the first (arr[j])
