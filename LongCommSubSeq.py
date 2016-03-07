# Longest comman subsequence between two strings

def max(a, b):
    return (a - ((a - b) & ((a - b) >> 31)))

def find(s1,s2):
    if (len(s1) == 0 or len(s2) == 0):
        return 0;
    if (s1[len(s1) - 1] == s2[len(s2) - 1]):
        c = 1 + find(s1[:len(s1) - 1], s2[:len(s2) - 1]);
    else:
        c = max (find(s1[:len(s1)], s2[:len(s2) - 1]),find(s1[:len(s1) - 1], s2[:len(s2)]));
    return c;
    
s1 = "";
s2 = "";
print find(s1, s2);