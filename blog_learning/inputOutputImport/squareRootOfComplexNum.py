import cmath
num=eval(input("Enter some complex number(Ex: a+bj) : "))
squareRootNum= cmath.sqrt(num)
print("Square root of given number {} is : \
	{}+{}j ".format(num,squareRootNum.real,squareRootNum.imag))
