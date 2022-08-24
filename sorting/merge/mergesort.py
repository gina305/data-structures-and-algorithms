 def mergeSort(sequence):
   n = len(sequence)

    if n > 1:
      
      mid= n//2
      left =  sequence[0:mid]
      right = [mid:-1]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)t
