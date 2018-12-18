# Custom operators
# 25 nov 2018 // LAMBDA UPDATE 18 dec 2018; fixed operator bug in multidot
# AR, AQ, Abdullah

star     = lambda op1, op2: op1*2 + op2
squiggle = lambda op1, op2: op1**3 + op2**2
multidot = lambda op1, op2: op1*4 // op2

print ("8 star 2 == ", star (8,2)) # == 18
print ("3 squiggle 2 == ", squiggle (3,2)) # == 31
print ("2 multidot 2 == ", multidot (2,2)) # == 4

print("\n")
