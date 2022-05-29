def sort(nums):        
    if len(nums) < 2:
        return nums
    else:
        m = len(nums)//2
        
        left = sort(nums[:m])
        right = sort(nums[m:])
        
        buf = merge(left, right, 0, 0, [])
        
        return buf

def merge(left, right, l, r, buf):

    if l < len(left) and r < len(right):
        if left[l] < right[r]:
            buf.append(left[l])
            return merge(left, right, l+1, r, buf)
                        
        else:
            buf.append(right[r])
            return merge(left, right, l, r+1, buf)
    
    if l < len(left):
        buf.append(left[l])
        return merge(left, right, l+1, r, buf)
         
    if r < len(right):
        buf.append(right[r])
        return merge(left, right, l, r+1, buf)
        
    return buf
        
a = [1,9,0,3,4,6]
print(a)
m = sort(a)
print(m)
