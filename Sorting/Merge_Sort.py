def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_sub = arr[:mid]
        right_sub = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left_sub)
        merge_sort(right_sub)
        
        # Merge the sorted halves
        i = j = k = 0
        
        # Compare elements from both halves and build the sorted array
        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] < right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1
        
        # Copy any remaining elements of left_sub
        while i < len(left_sub):
            arr[k] = left_sub[i]
            i += 1
            k += 1
        
        # Copy any remaining elements of right_sub
        while j < len(right_sub):
            arr[k] = right_sub[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    arr = [10, 11, 101, 45, 62, 12]
    res = merge_sort(arr)
    print(res)
