
def twoSum(a, t):
    map = {};
    
    for i in range(0,len(a) -1):
        if(map.has_key(a[i])):
            index1 = map.get(a[i]) + 1;
            index2 = i + 1;
            return index1, index2;
        else:
            map[t - a[i]] = i;
            
    

l = [2,3,6,11,10,15,7];
print "index1: %d index2: %d"%twoSum(l, 9);