#functions that will be used in our pendu.py programme

import configdata as cd #import the config file
from random import randrange

def random_word():
	"""
	Function to choose a random words from the txt files with the correct number of letters
	"""
	with open(cd.pendu_words_file) as f : # we read all the words contained in the file of words
		pendu_words = f.read().split("\n") 

	pendu_words = [word for word in pendu_words if len(word)==cd.max_letter] # we filter on the 8 length words only

	return pendu_words[randrange(len(pendu_words))] # we randomly choose the word from the pendu words list



def pos_letter(l, w):
	"""
	Function to get the position of a letter l in a word
	Return a list with the letter positions(s)
	"""
	pos_list = [pos for pos,char in enumerate(w) if char == l]
	return pos_list
