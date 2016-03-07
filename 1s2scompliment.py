#1's 2's compliment of binary number (given string format)

def flip(c):
    c = '1' if(c == '0') else '0';
    return c;

def solution(str):
    #1's compliment
    s = list(str);
    for i in range(0,len(s)):
        s[i] = flip(s[i]);
    str1 = ''.join(s);
    print ("1's Compliment is : %s"%str1);
    #2's compliment
    
    for i in range(0,len(s)):
        if(s[len(s) - 1 - i] == '0'):
            #index = i;
            s[len(s) - 1 - i] = 1;
            break;
        else:
            s[len(s) - 1 - i] = flip(s[len(s) - 1 - i]);
    #str2 = ''.join(str(s));
    print ("2's Compliment is : ", s);
    
str = "0111";
solution(str);
str1 = "1100";
solution(str1);
