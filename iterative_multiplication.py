def mult(a,b):
	prod = 0

	for i in range(b):
		prod += a

	return prod

print("Product: "+ str(mult(10,10)))