# check binary representation of integer is palindrom or not

def check(x,k):
    return 1 if (x & (1 << (k))) else 0;
    

def palinInt (n):
    l = 0;
    m = 31;
    while (l < m):
        if(check(n,l) != check(n,m)):
            return 0;
        l += 1;
        m -= 1;
    return 1;
    
n = 1 << 31 + 1;
print "Palindrom" if (palinInt(n)) else "Not Palindrom";

n = 1 << 31;
print "Palindrom" if (palinInt(n)) else "Not Palindrom";


n = 1<<15 + 1<<16;
print "Palindrom" if (palinInt(n)) else "Not Palindrom";