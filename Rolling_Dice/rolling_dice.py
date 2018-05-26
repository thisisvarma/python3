####		Rolling Dice program	######
import random

print(" \n##### We are currently at Rolling dice program #####\n")

#number_of_players=int(input("choose number of player you want"))
while True:
	rolling_dice_status=input("\ndo you like to roll Dice A and B (yes/no) : ")
	if rolling_dice_status == "yes" or rolling_dice_status == "no":
		print("\nyou choose : ", rolling_dice_status,"\n")
		break
	else:
		print("Invalid : Choose either yes or no") 
Dice_A_value=random.randrange(1,6)
Dice_B_value=random.randrange(1,6)
def rolling_dice():
	print("We are rolling dice A and B")
	print("Dice A value is : ",Dice_A_value)
	print("Dice B value is : ", Dice_B_value)
	print("Total Turn count is : ",Dice_A_value+Dice_B_value)
def not_rolling_dice():
	print("\nyou choosen - dont roll dice, So we are not rolling dice\n")
	print("\n\tGAME END\n\t")
while True:
	if rolling_dice_status == "yes":
		rolling_dice()
		break	
	elif rolling_dice_status == "no":
		not_rolling_dice()
		break
