

def mod(n,m):
	return n%m

def mod_inverse(n,m):
	for i in range(1,m):
		if ((n*i)%m)==1:
			return i
	return None

n = int (input("enter a number"))
m = int(input("enter the modulus"))

modulus = mod(n,m)
print(f"the modulus of {n} and {m} is {modulus}")
modulo_inverse = mod_inverse(n,m)
print(f"the modulo inverse of {n} and {m} is {modulo_inverse}")




