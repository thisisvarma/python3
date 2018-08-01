print(" ****** this program prints fruits from given list ***** ")


basket=["apple","banana","nuts","grapes","apple"]
item_order=0
for fruits in list(basket):
	if fruits == "nuts":
		item_order+=1
		continue
	item_order+=1
	print("item {} - fruit is {}".format(item_order,fruits))