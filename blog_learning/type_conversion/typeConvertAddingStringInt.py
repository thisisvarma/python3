# we are going to add string and int datatypes in this program

num_int=10
num_str="Hello Varma"

# logic 1 -> num_new=num_int+num_str
# logic 2

num_new = str(num_int) + num_str
print("to support this type of operations we will go with explicit type conversion")
print("the new value of num_new is :",num_new,\
	"type is :",type(num_new))

