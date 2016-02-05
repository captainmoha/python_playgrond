def prime1(n):
    
    if (n < 2):
    	return False

    i = 2
    while (i*i <= n):
    	if (n%i==0):
    		return False
    	i+=1
    return True

def prime2(n):

	if (n < 2):
		return False
	for i in range(2,n+1):
		if (i != n and n%i==0):
			return False
	return True
