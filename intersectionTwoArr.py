# find intersection of two array 
# Dictionary
# set
# Example [1 , 2, 3, 5, 10, 0, 5]
#		  [0, 1, 11, 10, 5, 5]
# result: [0, 1, 5, 10]

def intersectionSet(a, b):
	s = set(a);
	l = [];
	i = 0;
	while (i < len(b)):
		if (b[i] in s):
			l.append(b[i]);
			s.discard(b[i]);
		i += 1;
	return l;


def intersectionDic(a,b):
	map = {};
	i = 0;
	# build map
	while (i < len(a)):
		map[a[i]] = 0;
		i += 1;
	i = 0;
	l = [];
	while (i < len(b)):
		if(map.has_key(b[i])):
			l.append(b[i]);
			del map[b[i]];
		i += 1;

	return l;


def intersectionNArrDic(*arr):
	j = 1;
	for a in arr:
		i = 0;
		if (j == 1):
			map = {};
			# build map
			while (i < len(a)):
				map[a[i]] = 1;
				i += 1;
		else:
			while (i < len(a)):
				if(map.has_key(a[i])):
					if (map.get(a[i])  == j - 1):
						map[a[i]] = j;
				i += 1;
		# print a;
		# print map;
		j += 1;		
	# print j;	
	for (k,v) in map.items():
		if(v != j - 1):
			del map[k];
	return map.keys();

def intersectionNArrSet(*arr):
	j = 0;
	for a in arr:
		if (j == 0):
			s = set(a);
			temp = set();
			j = 1;
		else:
			# t = set(a);
			# for x in s:
			# 	if (x in t):
			# 		temp.add(x);

			i = 0;
			while (i < len(a)):
				if (a[i] in s and a[i] not in temp):
					print 
					temp.add(a[i]);
				i += 1;
			
			
			if (len(temp) == 0): break;
			s = temp.copy();
			temp.clear();
	return s;

a = [ 1, 0, 5, 10, 5, 6]
b = [0, 5, 11, 8, 30, 1]
c = [0, 1, 10, 6]
print "intersectionSet(a, b):",intersectionSet(a, b);
print "intersectionDic(a,b):",intersectionDic(a,b);
print "intersectionNArrDic(a, b, c):",intersectionNArrDic(a, b, c);
print "intersectionNArrSet(a,b,c):",intersectionNArrSet(a,b,c);