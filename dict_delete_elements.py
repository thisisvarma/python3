print("-------------dict_delete_elements---------------")

d={100:'santhosh',200:'varma',300:'kumar'}
print(d)
print("\n############Deleting value at key 100##############\n")
del d[100]
print(d)
#print("\n############Deleting value at key 400 ##############")
#del d[400]
#print(d)
print("\n############ clearing Dict ##############")
d.clear()
print(d)