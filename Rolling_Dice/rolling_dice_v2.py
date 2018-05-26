#version2 Rolling dice program
import random
while True:
	rolling_dice_status=input("\ndo you like to roll Dice A and B (yes/no) : ")
	if rolling_dice_status == "yes":
		repeat="yes"
		break
	elif rolling_dice_status == "no":
		print("You choose not to roll dices")
		repeat="no"
		break
	else:
		print("Invalid : Choose either yes or no")

while repeat == "yes":
	print("We are rolling dice A and B")
	Dice_A_value,Dice_B_value=random.randrange(1,6),random.randrange(1,6)
	print("Dice A value is : ",Dice_A_value)
	print("Dice B value is : ", Dice_B_value)
	print("Total Turn count is : ",Dice_A_value+Dice_B_value)
	repeat=input("Do you like to repeat rolling (yes/no) :")

