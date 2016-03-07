# power in O(logn) time
import time;

def power(n,d):
    
    if (d == 1):    #Base Condition
        return n;
    
    if (d%2 == 0):  #EVEN
        r = power(n, d/2)*power(n, d/2);
    else:   # ODD
        r = n*power(n,d/2)*power(n,d/2);
    return r;
    
def powerOld(n, d):
    if (d == 1):
        return n;
    r = n*power(n,d-1);
    return r;
    
n = 99;
d = 999;
t1 = (time.time());
print power(n,d);
t2 = (time.time());
print powerOld(n, d);
t3 = (time.time());

print "time taken by power(): ",(t2-t1),"time taken by powerOld()", (t3-t2);(time.time());