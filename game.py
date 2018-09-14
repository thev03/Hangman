import random

class Game:

	def __init__(self, word):
		self.word = word
		self.lives = 7
		self.goodGuesses = []

	def show_word(self):
		print " The word was " + self.word

	def show_lives(self):
		print "You have " + str(self.lives) + " lives"

	def hide_word(self):
		letters = []
		for character in self.word:
			letters.append("[_]")
		print "  ".join(letters)
	
	def get_letter(self):
		return raw_input("What is your letter?")
	
	def is_letter_in_word(self, letter):
		return letter in self.word

	def evaluate_guess(self, guess):
		if self.is_letter_in_word(guess):
			print "good guess!"
			self.goodGuesses.append(guess)
			self.replace_all_guessed_letters()
			self.after_good_guess()
		else:
			self.reduce_lives()			
			self.after_bad_guess()

	def after_good_guess(self):
		if len(self.goodGuesses) == len(self.word):
			print """YOU WON !!                                                                      <<<<||||||>>>>> FIREWORKS AND CONFETTI !!  :) <<<<||||||>>>>>"""
		if self.lives > 0 and len(self.goodGuesses) != len(self.word): 
			letter = self.get_letter()
			self.evaluate_guess(letter)

	def after_bad_guess(self):
		if self.lives > 0:
			print "Try again"
			letter = self.get_letter()
			self.evaluate_guess(letter)
		else:
			print "Game over"
			self.show_word()

	def reduce_lives(self):
		self.lives -= 1 
		print "you have lost a life, you now have " + str(self.lives)

	def game_is_over(self):
		self.lives == 0

	def replace_all_guessed_letters(self):
		convertedWord = []
		for character in self.word:
			if character in self.goodGuesses:
				convertedWord.append(character)
			else :
				convertedWord.append("[_]")
		print " ".join(convertedWord)

animals = ["duck", "hare", "wolf", "bear", "bird", "spider", "tiger", "chipmunk", "dolphin", "donkey"]
picked_animal = random.choice(animals)
our_game = Game(picked_animal)
our_game.show_lives()
our_game.hide_word()
letter = our_game.get_letter()
print letter
our_game.evaluate_guess(letter)







