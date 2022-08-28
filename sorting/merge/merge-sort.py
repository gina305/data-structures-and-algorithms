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

    a = a + 1
mergeSort()

