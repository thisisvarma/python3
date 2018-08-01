lower=eval(input("Enter lower limit value in range : "))
upper=eval(input("Enter upper limit value in range : "))
primelist=[]
for num in range(lower,upper+1):
	if num > 1:
		for i in range(2,num):
			#finding factors
			if (num % i) == 0:
				break
		else:
			primelist.append(num)
	else:
		print(num ,"is prime number")
print("number of prime number between {} and {} are {}".format(lower,upper,len(primelist)))
print(primelist)