player1 = input("Огонь (о), вода(в), брёвна(б)?")
from random import randint

comp = random_number = randint(0, 2)
if comp == 0 :
 	comp = "@"
if comp == 1:
 	comp = "/_/"
if comp == 2:
 	comp = "$"

if player1 == "о":
	player1 = "$"
elif player1 == "в":
	player1 = "/_/"
elif player1 == "б":
	player1 = "@"
print(player1)
print("vs")
print(comp)

if player1 =="@" and comp == "$":
	print("player1 wins")
elif player1 == "$" and comp == "/_/":
	print("player1 wins")
elif player1 == "/_/" and comp == "@" :
	print("player1 wins")
elif player1 == "@" and comp =="/_/":
	print("cpu wins")
elif player1 == "$" and comp == "@":
	print("cpu wins")
elif player1 == "/_/" and comp =="$":
	print("cpu wins")
elif player1 == "$" and comp =="$":
	print("draw")
elif player1 == "/_/" and comp =="/_/":
	print("draw")
elif player1 == "@" and comp =="@":
	print("draw")