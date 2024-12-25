def selection_sort(arr):
    if len(arr)==0:
        return []
    for i in range(0,len(arr)-1):
        min_ele = i
        for j in range(i+1,len(arr)-1):
            if arr[j]<arr[min_ele]:
                min_ele = j
        arr[i],arr[min_ele] = arr[min_ele],arr[i]
    return arr
