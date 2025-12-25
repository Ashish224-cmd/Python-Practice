def bubblesort(arr):
    n = len(arr)
    for i in range(0,n):
        swap = False 
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swap = True 
           
        if (swap==False):
            break 
    return arr
        
arr = [64,34,25,12,22,11,90]
res = bubblesort(arr)
print(res)