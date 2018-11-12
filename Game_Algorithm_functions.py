
def spin(wheel_dict):  # Chooses a "weighted" random integer that then decides the money value
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