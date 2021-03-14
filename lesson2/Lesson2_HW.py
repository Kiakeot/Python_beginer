player1 = input("Камень (к), ножницы(н), бумага(б)?")
from random import randint

comp = random_number = randint(0, 2)
if comp == 0 :
 	comp = "O"
if comp == 1:
 	comp = "8<"
if comp == 2:
 	comp = "-"

if player1 == "н":
	player1 = "8<"
elif player1 == "к":
	player1 = "O"
elif player1 == "б":
	player1 = "-"
print(player1)
print("vs")
print(comp)

if player1 =="O" and comp == "8<":
	print("player1 wins")
elif player1 == "8<" and comp == "-":
	print("player1 wins")
elif player1 == "-" and comp == "O" :
	print("player1 wins")
elif player1 == "O" and comp =="-":
	print("cpu wins")
elif player1 == "8<" and comp == "O":
	print("cpu wins")
elif player1 == "-" and comp =="8<":
	print("cpu wins")
elif player1 == "8<" and comp =="8<":
	print("draw")
elif player1 == "-" and comp =="-":
	print("draw")
elif player1 == "O" and comp =="O":
	print("draw")

