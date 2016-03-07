#if Check if an array can be divided into pairs whose sum is divisible by k
import math;
def func(a, t):
    map = {};
    
    for i in range(0, len(a)):
        #print i;
        if(map.has_key(a[i])):
            index1 = map.get(a[i]);
            index2 = i;
            print "( %d, %d)"%(a[index1],a[index2]);
        else:
            f = int(math.ceil(a[i]/6.0));
            #print t,f,a[i], t*f - a[i]
            map[t*f - a[i]] = i;
            #print map;
        
    
    
    # for i in range(0,len(a) -1):
        # if(map.has_key(a[i])):
            # index1 = map.get(a[i]) + 1;
            # index2 = i + 1;
            # return index1, index2;
        # else:
            # map[t - a[i]] = i;
             

l = [9,7,5,3,12,3];
func(l, 6);