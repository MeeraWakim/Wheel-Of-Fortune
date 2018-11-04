
import random
import sys

class player:

	def __init__(self,name):
		self.name = name
		self.score = 0

	def spin(self,wheel_dict):
		num = random.randint(1,281)
		value = 0
		if num <= 50:
			value = wheel_dict[1]
		elif num <= 100:
			value = wheel_dict[2]
		elif num <= 150:
			value = wheel_dict[3]
		elif num <= 200:
			value = wheel_dict[4]
		elif num <= 250:
			value = wheel_dict[5]
		elif num <= 275:
			value = wheel_dict[10]
		elif num <= 280:
			value = wheel_dict[100]
		else:
			value = wheel_dict[1000]
		return(value)

def showWord(phrase,guessed):

	print("Word: ")
	for i in range(len(phrase)):
		if phrase[i].lower() not in guessed and phrase[i].upper() not in guessed:
			if phrase[i] == " ":
				print("  ",end = " ")
			else:
				print("__", end = " ")
		else:
			print(phrase[i], end = " ")

def main():

	wheel_dict = {1 : 1000, 2 : 2000, 3 : 3000, 4 : 4000, 5 : 5000, 10 : 10000, 100 : 100000, 1000: 1000000}

	phraseFile = open("Phrases.txt", "r")
	phrases = []
	for line in phraseFile:
		if line.find("\n") != -1:
			phrases.append(line[:-1])
		else:
			phrases.append(line)

	num_players = input("Enter number of players: ")
	while True:
		if num_players.find(".") >= 0 or num_players.find("-") >= 0:
			num_players = input("You didn't type in a positive integer. Please try again: ")
		else:
			try:
				num_players = int(num_players)
				dummyNum = 2/num_players
				if num_players == 1:
					num_players = input("You cannot play by yourself! Please try again: ")
				else:
					break
			except ValueError:
				num_players = input("You didn't type in a positive integer. Please try again: ")
			except ArithmeticError:
				num_players = input("You didn't type in a positive integer. Please try again: ")
	print("")
	players = []

	for i in range(0,num_players):
		player_name = input("Player " + str(i + 1) + ", enter your name: ")
		players.append(player(player_name))

	num_phrases = input("\nThere are " + str(len(phrases)) + " phrases to choose from. Enter the number of phrases you want to guess: ")
	while True:
		if num_phrases.find(".") >= 0 or num_phrases.find("-") >= 0:
			num_phrases = input("You didn't type in a positive integer. Please try again: ")
		else:
			try:
				num_phrases = int(num_phrases)
				dummyNum = 2/num_phrases
				if num_phrases > len(phrases):
					num_phrases = input("There aren't " + str(num_phrases) + " phrases available. There are only " + str(len(phrases)) + ". Please try again: ")
				else:
					break
			except ValueError:
				num_phrases = input("You didn't type in a positive integer. Please try again: ")
			except ArithmeticError:
				num_phrases = input("You didn't type in a positive integer. Please try again: ")
	print("")

	for gameNum in range(num_phrases):

		notWin = True
		turn = random.randint(1,num_players - 1)
		num_guessedLetters = 0
		phrase = phrases[gameNum]
		guessed = []
		print("Phrase #" + str(gameNum + 1) + " out of " + str(num_phrases))
		print("--------------------------")

		while notWin:

			print("\nIt is " + players[turn].name + "'s turn.")
			dummy = input(" ~ Press Enter to spin the wheel ~ \n")

			value = players[turn].spin(wheel_dict)
			showWord(phrase,guessed)
			print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter.")
			guess = input("Letter: ")
			while True:
				if guess.isalpha():
					if len(guess) == 1:
						break
					else:
						guess = input("You didn't type in a single letter. Please try again: ")
				else:
					guess = input("You didn't type in a letter. Please try again: ")
			correct = True

			while correct:
				if (guess.lower() in phrase) or (guess.upper() in phrase):
					if guess in guessed:
						print("That letter has already been guessed.")
						correct = False
					else:
						players[turn].score += value
						guessed.append(guess)
						num_guessedLetters += 1
						if len("".join(set(phrase.replace(" ", "")))) == num_guessedLetters:
							print("Correct! Your now have $" + str(players[turn].score) + ".")
							print("\nThe phrase has been revealed by " + str(players[turn].name) + "!")
							print("The phrase was: " + phrase + "\n")
							if gameNum != num_phrases - 1:
								print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
							notWin = False
							correct = False
						else:
							print("Correct! Your now have $" + str(players[turn].score) + ". Spin again.")
							dummy = input(" ~ Press Enter to spin the wheel ~ \n")
							value = players[turn].spin(wheel_dict)
							showWord(phrase,guessed)
							print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter.")
							guess = input("Letter: ")
							while True:
								if guess.isalpha():
									if len(guess) == 1:
										break
									else:
										guess = input("You didn't type in a single letter. Please try again: ")
								else:
									guess = input("You didn't type in a letter. Please try again: ")
				else:
					print("Incorrect!")
					correct = False

			if turn < (num_players - 1):
				turn += 1
			else:
				turn = 0
	print("The game has concluded!")
	winningScore = 0
	for the_player in players:
		print(the_player.name + " ended with $" + str(the_player.score) + "!")
		if winningScore < the_player.score:
			winningScore = the_player.score

	winners = []
	for the_player in players:
		if winningScore == the_player.score:
			winners.append(the_player.name)
	if len(winners) == 1:
		print("\nThe winner is " + winners[0] + " with an ending amount of $" + str(winningScore) + "!")
	else:
		print("\nThere is a tie! The winners are:")
		for player_name in winners:
			print(player_name)
		print("They all ended with an amount of $" + str(winningScore) + "!")


main()