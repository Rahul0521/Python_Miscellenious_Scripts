def merge_sort(arr):
    if len(arr)>1:
        left_sub  = arr[:len(arr)//2]
        right_sub  = arr[len(arr)//2:]
        # print(left_sub,right_sub)
        merge_sort(left_sub)
        merge_sort(right_sub)
        i,j,k = 0,0,0
        while i<len(left_sub) and j<len(right_sub):
            if left_sub[i]<right_sub[j]:
                arr[k] = left_sub[i]
                i+=1
                k+=1
            else:
                arr[k] = right_sub[j]
                j+=1
                k+=1
        while i<len(left_sub):
            arr[k] = left_sub[i]
            i+=1
            k+=1
        while j<len(right_sub):
            arr[k] = right_sub[j]
            j+=1
            k+=1


    return arr

def merge_procedure(arr,i,mid,j):
    left_sub = arr[:mid]
    right_sub   = arr[mid:]
    p = 0
    q = 0
    k = i
    while p<len(left_sub)-1 and q<len(right_sub)-1:
        if left_sub[p]<=right_sub[q]:
            arr[k] = left_sub[p]
            p+=1
        else:
            arr[k] = right_sub[q]
            q+=1
    while p<len(left_sub):
        arr[k] = left_sub[p]
        p+=1
        k+=1
    while q<len(right_sub):
        q+=1
        k+=1
    return arr
if "__main__" == __name__:
    arr = [10,11,101,45,62,12]
    res = merge_sort(arr)
    print(res)
