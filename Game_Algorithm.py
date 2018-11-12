import random
import sys

# Global variables #
triviaIndex = 0  # Counter that goes through all the trivia questions
wheel_dict = {1 : 1000, 2 : 2000, 3 : 3000, 4 : 4000, 5 : 5000, 10 : 10000, 100 : 100000, 1000: 1000000}  # Possible prizes; key value 10 is bonus trivia question
guess = ""
correct = True

class player:

	def __init__(self,name):
		self.name = name
		self.score = 0

	def spin(self,wheel_dict):  # Chooses a "weighted" random integer that then decides the money value
		num = random.randint(1,281)  # Random integer from 1 - 281, inclusive
		value = 0
		if num <= 50:  # 1 - 50
			value = wheel_dict[1]
		elif num <= 100:  # 51 - 100
			value = wheel_dict[2]
		elif num <= 150:  # 101 - 150
			value = wheel_dict[3]
		elif num <= 200:  # 151 - 200
			value = wheel_dict[4]
		elif num <= 250:  # 201 - 250
			value = wheel_dict[5]
		elif num <= 275:  # 251 - 275
			value = wheel_dict[10]
		elif num <= 280:  # 276 - 280
			value = wheel_dict[100]
		else:  # 281
			value = wheel_dict[1000]
		return(value)

def showWord(phrase,guessed):  # Displays the phrase with the letters that haven't been guessed yet removed

	print("Word: ")
	guessedPhrase = ""
	for i in range(len(phrase)):
		if phrase[i].lower() not in guessed and phrase[i].upper() not in guessed:  # If the guessed letters are not in the list containing the list of correctly guessed letters
			if phrase[i] == " ":  # Whitespace
				print("  ",end = " ")
				guessedPhrase += " "
			else:
				print("__", end = " ")
				guessedPhrase += " __ "
		else:
			print(phrase[i], end = " ")  # Print the letter from the original phrase
			guessedPhrase += phrase[i]
	return guessedPhrase

def trivia(players, triviaQs, randomTriviaIndices, value, turn, phrase, guessed):

	global triviaIndex
	global guess
	global wheel_dict
	global correct

	print(players[turn].name + " has landed on a bonus tile! Trivia time!")
	if triviaIndex == len(triviaQs) - 1:  # If all the trivia questions have been answered already
		random.shuffle(randomTriviaIndices)  # Shuffle them again
		triviaIndex = 0  # Start back at the first trivia question (whatever that may be)
	print("----------------------------------------------------------------------------------------")
	letters = ["A: ", "B: ", "C: ", "D: "]
	for i in range(5):
		if i == 0:
			print(triviaQs[randomTriviaIndices[triviaIndex]][i] + "\n")
		else:
			print(letters[i-1] + triviaQs[randomTriviaIndices[triviaIndex]][i])
	print("")

	triviaAnswer = input("Enter your answer: ")
	while True:  # Checking if the user entered a single letter (uppercase or lowercase)
		if triviaAnswer.isalpha():
			if len(triviaAnswer) == 1:
				if triviaAnswer.upper() == "A" or triviaAnswer.upper() == "B" or triviaAnswer.upper() == "C" or triviaAnswer.upper() == "D":
					break
				else:
					triviaAnswer = input("Invalid answer choice. Type \"A\", \"B\", \"C\", or \"D\". Please try again: ")
			else:
				triviaAnswer = input("You didn't type in a single letter. Please try again: ")
		else:
			triviaAnswer = input("You didn't type in a letter. Please try again: ")
	if triviaAnswer == triviaQs[randomTriviaIndices[triviaIndex]][5].lower() or triviaAnswer == triviaQs[randomTriviaIndices[triviaIndex]][5].upper():
		print("Correct! You win $100,000! Congratulations!")
		players[turn].score += value  # Player gets prize
		print("----------------------------------------------------------------------------------------")

		while value == 100000:
			value = players[turn].spin(wheel_dict)
		showWord(phrase,guessed)
		print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter.")
		guess = input("Letter: ")
		while True:  # Checking if the user entered a single letter (uppercase or lowercase)
			if guess.isalpha():
				if len(guess) == 1:
					break
				else:
					guess = input("You didn't type in a single letter. Please try again: ")
			else:
				guess = input("You didn't type in a letter. Please try again: ")
		correct = True
	else:
		print("Incorrect! The correct answer was " + triviaQs[randomTriviaIndices[triviaIndex]][5].upper() + ".")
		print("----------------------------------------------------------------------------------------")
		correct = False
	triviaIndex += 1

def main():  # Main program

	global triviaIndex
	global guess
	global wheel_dict
	global correct

	phraseFile = open("Phrases.txt", "r")
	phrases = []
	for line in phraseFile:
		if line.find("\n") != -1:  # Not the last phrase in the document
			phrases.append(line[:-1])
		else:  # Last phrase in document
			phrases.append(line)
	randomPhraseIndices = [i for i in range(len(phrases))]  # Indices that'll be used to randomly choose a phrase from the list phrases
	random.shuffle(randomPhraseIndices)

	triviaFile = open("Trivia.txt", "r")
	triviaQs = []
	lineCounter = 0  # Counting the number of lines processed to fit into triviaQ
	triviaQ = []
	for line in triviaFile:
		if line.find("\n") != -1:
			triviaQ.append(line[:-1])
		else:
			triviaQ.append(line)
		lineCounter += 1
		if lineCounter == 6:
			triviaQs.append(triviaQ)
			lineCounter = 0
			triviaQ = []
	randomTriviaIndices = [i for i in range(len(triviaQs))]  # Indices that'll be used to randomly choose a trivia question from the list triviaQs
	random.shuffle(randomTriviaIndices)

	num_players = input("Enter number of players: ")
	while True:  # Checking if the user inputted a positive integer
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
		players.append(player(player_name))  # Appends created player object to players

	num_phrases = input("\nThere are " + str(len(phrases)) + " phrases to choose from. Enter the number of phrases you want to guess: ")
	while True:  # Checking if the user inputted a positive integer
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

	for gameNum in range(num_phrases):  # Looping over the chosen phrases

		notGuessed = True  # No one completed the phrase yet
		turn = random.randint(1,num_players - 1)  # Chooses a random player to start off
		num_guessedLetters = 0
		phrase = phrases[randomPhraseIndices[gameNum]]
		guessed = []
		print("Phrase #" + str(gameNum + 1) + " out of " + str(num_phrases))
		print("--------------------------")

		while notGuessed:  # While the phrase hasn't been guessed yet

			print("\nIt is " + players[turn].name + "'s turn.")
			dummy = input(" ~ Press Enter to spin the wheel ~ \n")

			value = players[turn].spin(wheel_dict)
			if value == 100000:
				trivia(players, triviaQs, randomTriviaIndices, value, turn, phrase, guessed)
			else:
				showWord(phrase,guessed)
				print("\n" + players[turn].name + ", for $" + str(value) + ", guess a letter.")
				guess = input("Letter: ")
				while True:  # Checking if the user entered a single letter (uppercase or lowercase)
					if guess.isalpha():
						if len(guess) == 1:
							break
						else:
							guess = input("You didn't type in a single letter. Please try again: ")
					else:
						guess = input("You didn't type in a letter. Please try again: ")
				correct = True

			while correct:  # While the player is correct
				if (guess.lower() in phrase) or (guess.upper() in phrase):  # If the letter (upper or lowercase) is in the phrase
					if guess in guessed:  # If the letter has already been guessed
						print("That letter has already been guessed.")
						correct = False
					else:
						players[turn].score += value  # Player gets prize
						guessed.append(guess)  # Letter is now guessed
						num_guessedLetters += 1
						if len(list(set(phrase.lower().replace(" ", "")))) == num_guessedLetters:  # If the number of guessed letters equals the number of UNIQUE letters in the phrase
						# Quit the two while loops (one for correct, one for notGuessed)
							print("Correct! Your now have $" + str(players[turn].score) + ".")
							print("\nThe phrase has been revealed by " + str(players[turn].name) + "!")
							print("The phrase was: " + phrase + "\n")
							if gameNum != num_phrases - 1:  # If it isn't the last phrase
								print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
							notGuessed = False
							correct = False  # Really means to quit asking the user for letters
						else:  # If there are still letters to be guessed
							print("Correct! Your now have $" + str(players[turn].score) + ". Spin again.")
							dummy = input(" ~ Press Enter to spin the wheel ~ \n")
							value = players[turn].spin(wheel_dict)
							if value == 100000:
								trivia(players, triviaQs, randomTriviaIndices, value, turn, phrase, guessed)
							else:
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
				else:  # Player guessed incorrectly
					print("Incorrect!")
					correct = False

			if turn < (num_players - 1):  # If the last player hasn't been reached yet
				turn += 1  # Next player
			else:  # The last player has been reached
				turn = 0  # Back to player 1
	print("The game has concluded!")
	winningScore = 0
	for the_player in players:  # Calculating the winning score
		print(the_player.name + " ended with $" + str(the_player.score) + "!")
		if winningScore < the_player.score:
			winningScore = the_player.score

	winners = []  # In case of ties
	for the_player in players:
		if winningScore == the_player.score:
			winners.append(the_player.name)
	if len(winners) == 1:  # Only one winner
		print("\nThe winner is " + winners[0] + " with an ending amount of $" + str(winningScore) + "!")
	else:  # There was a tie!
		print("\nThere is a tie! The winners are:")
		for player_name in winners:
			print(player_name)
		print("They all ended with an amount of $" + str(winningScore) + "!")


main()