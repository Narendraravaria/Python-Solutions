import random ;

#print random.randint(1,10);

def swap(a,b):
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    return a,b


def partition(a,l,r):
    p = random.randint(l,r);
    [a[p], a[r]] = swap(a[p],a[r]);
    i = l;
    j = r-1 ;
    pivot = a[r];
    done = False;
    while (not done):
        while(i <= j and a[j] >= pivot):
            j -= 1;
        while(i <= j and a[i] <= pivot):
            i += 1;
        if i > j:
            done = True;
        else:
            [a[i],a[j]] = swap (a[i],a[j]);
        
    [a[i],a[j]] = swap (a[i],a[j]);
        
    return j;


def QuickSort(a,l,r):
    if(l < r):
        q = partition(a, l, r);
        QuickSort(a, l, q-1);
        QuickSort(a, q+1, r);
    
    
a = [1, 2, 5, 3, 7, 8, 4, 10];
QuickSort(a,0,len(a)-1);
print a;




