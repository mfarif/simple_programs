def sort(a):
    h = []
    for e in a: 
        h.append(e)
        heapify(h, len(h) - 1)
    return h
    
def heapify(a, i):
# parent = floor[(i -1)/2]
    p = int((i-1)/2)
# left  = 2*i + 1
# right = 2*i + 2
    l = (2 * i) + 1 
    r = (2 * i) + 2
    #if exist_parent and a[i] > a[p] then swap.
    while p < len(a) and a[i] > a[p]:
        a[i], a[p] = a[p], a[i]
        i = p
# i =  0 1 2 3 4 5
a = [1,9,0,3,4,6]
print(a)
h = sort(a)
print(h)
#       0
#      1             2
#   3    4        5      6
#  7  8  9 10   11 12  13 14
 
