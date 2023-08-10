from random import choice

def word_list(file_input):
	words = []
	with open(file_input, 'r') as file:
		for line in file:
			words.append(line.strip())	
	return words

def random_word(list_of_words):
	random_word = choice(list_of_words)
	return random_word

def is_real_word(guess, word_list):
	if guess in word_list:
		return True
	return False

def check_guess(guess, word_to_guess):
	result = ''
	for char in guess:
		if char not in word_to_guess:
			result += "_"
		elif char in word_to_guess:
			if guess.find(char) == word_to_guess.find(char):
				result += 'X'
			else:
				result += 'O'
	return result

def next_guess(word_list, guess):
	guess_fixed = guess.lower()
	if guess_fixed in word_list:
		return guess_fixed 
	else:
		new_guess = input('Please try again, words must have five letters: ')
		return next_guess(word_list, new_guess)

def play():
	words = word_list('5_letter_words.txt')
	word_to_guess = random_word(words)
	for i in range(6):
		guess = next_guess(words, input("Please guess a five letter word: "))
		print(check_guess(guess, word_to_guess))
		if guess == word_to_guess:
			print("You win!")
			return
	print(f"You lost! \n The word was {word_to_guess}")

play()