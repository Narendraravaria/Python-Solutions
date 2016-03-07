# [0,0,4,0,2,1,1,0] i/p
# [0,0,0,0,4,2,1,1] o/p

def func(a):
    i = len(a) - 1;
    j = len(a) - 1;
    while (i >= 0):
        if( i == j):
            if (a[j] == 0):
                i -= 1;
            else:
                i -= 1;
                j -= 1;
        else:
            if(a[j] == 0 and a[i] != 0):
                a[j] = a[j]^a[i];    #t = a[j]; #
                a[i] = a[j]^a[i];       #a[j] = a[i]; #
                a[j] = a[j]^a[i];       #a[i] = t; #
                i -= 1;
                j -= 1;
            elif (a[j] == 0 and a[i] == 0):
                i -= 1;
            else:       #(a[j] != 0 and a[i] == 0) will never occure
                i -= 1;
                j -= 1;
    return a;            

x = [0, 0, 4, 0 ,2, 1, 1, 0];
print "INPUT: ",x
print "OUTPUT: ", func(x);

x1 = [0, 0, 0, 0 ,0, 0, 0, 0];
print "INPUT: ",x1
print "OUTPUT: ", func(x1);

x2 = [4, 0, 0, 0 ,0, 0, 0, 4];
print "INPUT: ",x2
print "OUTPUT: ", func(x2);

x3 = [4, 4, 4, 2 ,1, 4, 1, 5];
print "INPUT: ",x3
print "OUTPUT: ", func(x3);

x4 = [4, 0, 0, 0 ,-1, 0, 0, 0];
print "INPUT: ",x4
print "OUTPUT: ", func(x4);

