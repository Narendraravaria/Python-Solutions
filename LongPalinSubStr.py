# Longest Palindromic Substring O(n2) Dynamic Programming
#import numpy

def palindromicSubStr(a):
    currLen = 1;
    maxLen = 1;
    startIn = 0;
    endIn = 0;
    # T = numpy.array(numpy.empty());
    t = [[1, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0],[0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 1]];
    
    while (currLen <= len(a)):
        for i in range(0,len(a) - (currLen -1)):        
            j = i + currLen -1;
            # print "len= %d,i= %d ,j= %d"%(currLen,i,j);
            if(a[i] == a[j]):
                if (i == j):
                    t[i][j] = 1;
                else:
                    if (t[i+1][j-1] == 1):
                        t[i][j] = 2 + maxLen;
                        maxLen = t[i][j];
                        startIn = i;
                        endIn = j;
                    else:
                        t[i][j] = 0;
            
        currLen += 1;
    return maxLen,startIn,endIn;           
                
s = "agbdba";
[l , i, j] = palindromicSubStr(s);
print "Palindromic substring in string '",s,"'is: '",s[i:j+1],"'\n& Palindrom Lenght is: ",l;
