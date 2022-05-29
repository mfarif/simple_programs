def sort(a):
    h = max_heap(a, len(a) - 1)
    n = len(h) - 1

    while(n > 0):
        h[0],h[n] = h[n],h[0] 
        max_heap(h, n-1)
        n -= 1
        
    return h  
    
def max_heap(a, i):

    while(i >= 0): 
        heapify(a, i)
        i -= 1
    return a
    
def heapify(a, i):
    # parent = round[(i -1)/2]
    p = int((i-1)/2)
    #if exist_parent and a[i] > a[p] then swap.
    if p < len(a) and a[i] > a[p]:
        a[i], a[p] = a[p], a[i]
        i = p
        heapify(a, i)
        
a = [1,9,0,3,4,6]
print("pre:",a)
h = sort(a)
print("post:",h)

