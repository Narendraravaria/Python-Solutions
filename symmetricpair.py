

def func(l):
    map = {};
    result = [];
    k = 0;
    for i in range(0, len(l)):
        #print l[i], " ", l[i][1]," ", map.has_key(l[i][1]);
        if(map.has_key(l[i][1])):
            if (l[i][0] == map.get(l[i][1])):
                result.append((l[i][1], l[i][0], i));
                #print result;
            else:
                map[l[i][0]] = l[i][1];
        else:
            map[l[i][0]] = l[i][1];
            #print map;
            
    return result;      
            
l = [(50,20), (10,5), (30,40),(40,30),(5,10)];
print "Input: ",l;
print func(l);
