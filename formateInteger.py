
def convertGen ():
    
def convert(num,c = 0):
    s = "";
    if (int(num/10) == 0):
        #return (c - 1, s+str(num)+",") if (c % 3 == 0) else c - 1, s+str(num);
        if(c %3 == 0):
            return c - 1, s+str(num)+",";
        else:
            return c - 1, s + str(num);
    [c,s1] = convert(int(num/10),c + 1);
    s = s + s1;
    if (c !=0 and c %3 == 0):
        s = s+str(num%10)+",";
    else: 
        s = s+str(num%10);
        
    return c - 1,s;
    
    

def formatInt(num):
    [c, s] = convert(num);
    return s;
 
num = 1234567;    #12,345
print formatInt(num);

    