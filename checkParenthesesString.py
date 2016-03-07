# Check whether a given string has valid parentheses

def checkUsingMap(s):
    map1 = {"{" : 0, "[" : 0, "(" : 0 };
    map2 = {"}" : "{", "]" : "[", ")" : "("};
    i = 0
    while (i < len(s)):
        if(s[i] == "{" or s[i] == "[" or s[i] == "(" ):
            map1[s[i]] += 1;
        elif (s[i] == "]" or s[i] == "}" or s[i] == ")"):
            t = map2.get(s[i]);
            map1[t] -= 1;
            if (map1[t] < 0):
                return 0;
        i += 1;
    for x in map1.values():
        if(x != 0):
            return 0;
    return 1;
    
    
s = "{}{{[[(}]])())(}";
#s = "{}[]()"
print checkUsingMap(s);