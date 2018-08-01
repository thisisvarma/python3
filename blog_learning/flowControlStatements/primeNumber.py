print(" prime number finder")
num=eval(input("Enter some number : "))

if num > 1:
	for i in range(2,num):
		#finding factors
		if (num % i) == 0:
			print("num is not a prime number")
			break
	else:
		print("number is prime number")

else:
	print("number is not a prime number")

