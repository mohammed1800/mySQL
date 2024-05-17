def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        
        # One final comparison when arr[j] <= key or j < 0
        if j >= 0:
            comparisons += 1
            
        arr[j + 1] = key
    
    return arr, comparisons

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr, total_comparisons = insertion_sort(arr)

print("Sorted array:", sorted_arr)
print("Total number of comparisons:", total_comparisons)
