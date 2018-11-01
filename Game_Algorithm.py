
import random
import sys

class player:

	def __init__(self,name):
		self.name = name
		self.score = 0

	def spin(self,wheel_dict):
		num = random.randint(1,2)
		return(wheel_dict[num])

def showWord(phrase,guessed):

	print("Word: ")
	for i in range(len(phrase)):
		if phrase[i] not in guessed:
			if phrase[i] == " ":
				print("  ",end = " ")
			else:
				print("__", end = " ")
		else:
			print(phrase[i], end = " ")

def main():

	wheel_dict = {1 : 1000, 2 : 2000}
	phrase = "garrett odom"
	guessed = []

	num_players = int(input("Enter number of players: "))
	players = []

	for i in range(0,num_players):
		print("Player " + str(i + 1) + ", enter your name: ")
		player_name = input("Name: ")
		players.append(player(player_name))

	notWin = True
	turn = random.randint(1,num_players - 1)
	while notWin:

		print("It is " + players[turn].name + "'s turn.")
		dummy = input(" ~press enter to spin the wheel~ \n")

		value = players[turn].spin(wheel_dict)
		showWord(phrase,guessed)
		print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter: ")
		guess = input("Letter: ")
		correct = True

		while correct:
			if (guess in phrase):
				if guess in guessed:
					print("That letter has already been guessed.")
					correct = False
				else:
					players[turn].score += value
					guessed.append(guess)
					print("Correct! Your now have $" + str(players[turn].score) + ". Spin again.")
					dummy = input(" ~press enter to spin the wheel~ ")
					value = players[turn].spin(wheel_dict)
					showWord(phrase,guessed)
					print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter: ")
					guess = input("Letter: ")
			else:
				print("Incorrect!")
				correct = False

		if turn < (num_players - 1):
			turn += 1
		else:
			turn = 0


main()










