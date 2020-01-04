from fractions import Fraction

def addFraction(num1, den1, num2, den2):
	return Fraction(num1, den1) + Fraction(num2,den2)

# test the function

print(addFraction(1,500,2,500))