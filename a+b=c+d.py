#Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) 
#such that a+b = c+d, and a, b, c and d are distinct elements. 
#If there are multiple answers, then print any of them.

def func (l):
    map = {};
    for i in range(0, len(l) -1):
        for j in range(i+1, len(l)):
            if(map.has_key(l[i] + l[j])):
                t1 = map.get(l[i] + l[j]);
                t2 = [l[i] , l[j]] if (l[i] < l[j]) else [l[j] , l[i]];
                #t = [l[i], l[j]];
                #t.sort();
                if (t1[0] != t2[0] and t1[1] != t2[1]):
                    return t1, t2;
                    #print t1 , " = ", t2;
                    #break;
            else:
                temp = [l[i] , l[j]] if (l[i] < l[j]) else [l[j] , l[i]];
                #temp = [l[i], l[j]];
                #temp.sort();
                map[l[i] + l[j]] = temp;
                print map;
    print len(map)
    
array = [3, 4, 7, 1, 2, 9, 8];
print "a + b = c + d"
print func(array);

