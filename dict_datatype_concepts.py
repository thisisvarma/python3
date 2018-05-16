print("------ the general concepts of Dictionary data type ------")

print('''

This is very regular usage datatype

Each element in this datatype will value one KEY and VALUE


Creation of Dict datatype:
---------------------------

Empty set is alway considered as Dict data type only

Example: 

run 	->	"program 1"

Key and value Example

run		->	"program 2"

''')

#program 1
data={}
print("the type of empty set is : ",type(data))

#program 2
data1={'RedHat':'Linux','Ubuntu':'Debian','Windows':'Microsoft'}
Recent_OS_release={7.5:'Linux-Redhat',18.1:'Debian-Ubuntu',10:'Microsoft-windows'}
print(type(data1))
print(data1)
print(type(Recent_OS_release))
print(Recent_OS_release)


print("Get value based on Key, Example : \nRecent_OS_release version 7.5 is : ", Recent_OS_release[7.5])