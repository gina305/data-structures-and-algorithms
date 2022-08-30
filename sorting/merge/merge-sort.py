a=0
  
def mergeSort(sequence=[8,4,23,42,16,15],t=""):

  n = len(sequence)
  global a 
  

  if n > 1:
    #print(f'Output for pass {a}')
    mid= n//2
    left =  sequence[:mid]
   # print(f'left list: value {left}')
    right = sequence[mid:]
    #print(f'right list value: {right}')
    
    # sort the left side
    mergeSort(left, "left")
      
    # // sort the right side
    mergeSort(right,"right")

    merge(left, right, sequence)

  



    a = a + 1
def merge(left, right, arr):
  i = 0
  j = 0
  k = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      j = j + 1

      k = k + 1

    if i == len(left):
      arr.append(left)
        

