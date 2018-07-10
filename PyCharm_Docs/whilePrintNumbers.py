limit=eval(input("Enter limit value : "))
n=0
while n < limit:
    print(n)
    n+=1

for i in range(limit):
    print(i)

mysum=0
for temp in range(2,10,2):
    print("temp value is : ", temp)
    mysum+=temp
    print(mysum)
print("sum of Even numbers from 1 to 10 is :", mysum)