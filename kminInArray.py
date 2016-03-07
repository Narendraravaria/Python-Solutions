# find k minimum in an array

def swap (x, y):
    x = x^y;
    y = x^y;
    x = x^y;
    return x,y;

def bubbleSort(a,k = 0):
    print a;
    for i in range(0, k):
        for j in range(0, len(a)-1 - i):
            if (a[j] < a[j + 1]):
                [a[j], a[j+1]] = swap(a[j], a[j + 1]);
             
    print a;
    print a[len(a) - k:];

    
    
    
a = [1,2,5,7,3,1,9,10];
k = 3;
bubbleSort(a, k);