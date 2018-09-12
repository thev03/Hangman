class Game:

	def __init__(self, word):
		self.word = word
		self.lives = 7

	def show_word(self):
		print self.word

	def show_lives(self):
		print "You have " + str(self.lives) + " lives"

	def hide_word(self):
		letters = []
		for character in self.word:
			letters.append("[_]")

		print "  ".join(letters)
	
	#letter_entered = []
	def get_letter(self):
		return raw_input("What is your letter?")
	
	def is_letter_in_word(self, letter):
		return letter in self.word

	def evaluate_guess(self, guess):
		
		if self.is_letter_in_word(guess):
			print "good guess!"
			 #show the letter in the right place
		else:
			self.reduce_lives()			
			if self.lives > 0:
				print "Try again"
				self.get_letter()
			else:
				print "Game over"

			

	def reduce_lives(self):
		self.lives -= 1 
		print "you have lost a life,you now have " + str(self.lives)

	def game_is_over(self):
		self.lives == 0

	#def show_letter(self):
		#for character in self.word:
			#letters.append(letter_entered)

our_game = Game("mouse")
#our_game.show_word()
our_game.show_lives()
our_game.hide_word()
letter = our_game.get_letter()
print letter
our_game.evaluate_guess(letter)







