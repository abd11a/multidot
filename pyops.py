# Custom operators
# 25 nov 2018
# AR, AQ, Abdullah

def star_op (firstop, secondop):
	return ( firstop * 2) + secondop

def squiggle_op (firstop,secondop):
	return firstop**3 + secondop**2

def multidot (op1,op2):
	return	(op1*4)//op2	

print ("8 starop 2 == ", star_op (8,2)) # == 18
print ("3 squiggle 2 == ", squiggle_op (3,2)) # == 31
print ("2 multidot 2 == ", multidot(2,2)) # == 4

print("\n")
