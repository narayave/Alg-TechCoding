# Permutation palindrome
# CTCI - pg. 91

a = 'tact coab'
b = 'tact coa'

a = a.replace(' ','')
dict = {}

for i in a:
	if i in dict:
		dict[i] = (dict[i] + 1) % 2
	else:
		dict[i] = 1

print(dict)
vec = list(dict.keys())
print (vec)

count = 0

for i in dict:
	count += dict[i]

print(count)

print(True if count == (0 or 1) else False)