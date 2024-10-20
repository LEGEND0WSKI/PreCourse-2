# Python program for implementation of Quicksort Sort 
#   O(nlog(n)) Time complexity
# give you explanation for the approach
def partition(arr,low,high):                    
    #write your code here
    i = low
    j = high - 1
    pivot = arr[high]

    while i < j:
        while i < high and arr[i] <pivot:    # i moves from left to right
            i +=1

        while j > low and arr[j] >= pivot:   # j moves from right to left
            j -= 1

        if i < j:                            # after j crosses i 
            arr[i],arr[j] = arr[j],arr[i]    # swap

    if arr[i] > pivot:                       # after i crosses pivot
        arr[i],arr[high] = arr[high],arr[i]  # swap pivot location
    
    return i

    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:                                  #recursion base case 
        pivot = partition(arr,low,high)             #return new pivot  
        quickSort(arr,low,pivot-1)                  #sort left subarray of pivot
        quickSort(arr,pivot+1,high)                 #sort right subarray of pivot

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "), 
  
 
