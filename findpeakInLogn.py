# find a peak using binary search (O(log(n)))

def findPeak(a):
    mid = int(len(a)/2);
    if(mid == 0 or mid == len(a) - 1):
        return a[mid];
    
    if (a[mid] >= a[mid + 1] and a[mid] >= a[mid - 1]):
        return a[mid];
    elif (a[mid] < a[mid - 1]):     #left
        return findPeak(a[:mid]);
    else:
        return findPeak(a[mid+1:]);
        
        
a = [1 ,3, 6,3 , 7 ,8];
print findPeak(a);