print("-------------Remove duplicate elements from list-------------------")

#method 1

list=eval(input("enter some list with [] : "))
list1=[]
for temp in list:
	if temp not in list1:
		list1.append(temp)
print("unique elements from entered list is : ",list1)


#method 2

print('''
	method 2 is not recommonded because it doesnt preserve order of elements
	''')
list2=set(list)
print("removing duplicates using set function", list2)