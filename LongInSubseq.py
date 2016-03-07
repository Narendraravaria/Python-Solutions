# Longest increasing susequesnce in O()n^2) time

def findLongInSubseq(a):
    uptillMax = 1;
    t = [];
    t.append(1);
    i = 1;
    j = 0;
    while (i <= len(a) - 1):
        t.append(1);
        while (j < i):
            if (a[i] > a[j]):
                t[i] = maxBin (t[i], t[j] + 1);
                uptillMax = maxBin(uptillMax, t[i]);
            j += 1;
        j = 0;
        i += 1;
    print t;
    print "Max: ", uptillMax
            
def max(a,b):
    return a if (a > b) else b;


def maxBin(a,b):
    return (a - ((a - b) & ((a - b) >> 31)));
    
def minBin (a, b):
    return (a + ((b - a) & ((b - a) >> 31)));

l = [3,4,-1,0,5,10,7,11];
print l;
findLongInSubseq(l);

a = 5;
b = 3;
print "min of a = %d and b = %d is %d"%(a, b, minBin(a,b));