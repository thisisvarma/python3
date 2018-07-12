print("\n ****** membership Operator examples **** ")

print('''

in		-->	True if value or variable presents in list, string,tuple or dict
not in	-->	True if value or variable not presents in list, string, tuple or dict

''')


x=input("enter string what ever you like : ")

y="aeiou"


print("'H' in x is : ",'H' in x)
print("'Hellow' in x is : ",'Hellow' in x)
print("'Hellow' not in x is : ",'Hellow' not in x)


for i in list(y):
	if i in x:
		print(i, "presents in ",x)
