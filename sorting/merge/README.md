# Blog Notes: Merge Sort

Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.


```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

       
Sample Arrays
In your blog article, visually show the output of processing this input array:

[8,4,23,42,16,15]

For your own understanding, consider also stepping through these inputs:

Reverse-sorted: [20,18,12,8,5,-2]
Few uniques: [5,12,7,5,5,7]
Nearly-sorted: [2,3,5,7,13,11]

### Implementation
Provide a visual step through for each of the sample arrays based on the provided pseudo code
Convert the pseudo-code into working code in your language
Present a complete set of working tests

### Trace

A sequence (such as an list) is passed into the mergeSort function.

The value of n is set to the length of the sequence.

A condition  for checking whether or not n is greater than 1 is checked.

If n (meaning the length of the sequence) is greater than 1, set the mid variable to the output of n divided by 2 (using floor division).

Pass 1:

Set the left list to the value of the sequence from the beginning index to the mid index.
```
left = [ 8,4,23]
```

Set the right list to the value of the sequence from the mid index to the last index. 
```
right = [ 42,16,15]
```
Call the mergeSort function for the left list.

Pass 2:
```
input: [8, 4, 23]

output:
left list: value [8]
right list value: [4, 23]
```
Pass 3:
```
input: [4, 23]

output: 
left list: value [4]
right list value: [23]
```

*The mergesort function will no longer be called on the left list because its length is not greater than 2


Pass 4:

Call the mergesort function on the right list:
```
Input: [42, 16, 15]

Output: 
left list: value [42]
right list value: [16, 15]
```

Pass 5:

Call the mergesort function on the right list again:
```
Input: [16,15]

Output:
left list: value [16]
right list value: [15]
```
*The mergesort function will no longer be called on the left list because its length is  not greater than 2.


### Efficency

Time: O(logN):The sequence is divided into two seperate sequences. Each sequence has nodes that are iterated on based on the sequence length, which is N. Therefore, the total time complexity is O(logN).

Space: O(N): The initial sequence is divided into two smaller sequences, which increases the space required for processing. Therefore, it gives us O(N).