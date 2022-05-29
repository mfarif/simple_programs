# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def sort(a):
    
    p = len(a)//2
    if p*2 > 1:
        la = sort(a[:p])
        ra = sort(a[p:])

        return merge(la, ra, 0, 0, [])
    else:
        return a
        
def merge(la, ra, l, r, buf):
    if(l < len(la) and r < len(ra)):
        if la[l] < ra[r]:
            buf.append(la[l])
            return merge(la, ra, l+1, r, buf)
        else:    
            buf.append(ra[r])
            return merge(la, ra, l, r+1, buf)
    if l < len(la):
        buf.append(la[l])
        return merge(la, ra, l+1, r, buf)
    if r < len(ra):
        buf.append(ra[r])
        return merge(la, ra, l, r+1, buf)
        
    return buf    
a = [4,5,1,2,9]
print(a)
a = sort(a)
print(a)
