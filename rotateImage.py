
# Codefights


def rotateImage(a):
	n = len(a)
	b = [[0 for x in range(n)] for y in range(n)]
	for i in range(n):
		for j in range(n):
			b[j][n-i-1] = a[i][j]
	return(b)



def rotateImage(a):
	return [[a[i][j] for i in range(len(a)-1,-1,-1)] for j in range(len(a))]

