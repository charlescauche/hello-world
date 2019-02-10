# main pendu programme


import configdata as cd #import the config file
import fonctions as func #import the fonctions.py functions

print("Start of the game...")
print("Programme is choosing a word")
word = func.random_word()
display = ["*" for l in range(len(word))]
print("the word is : ", display)


letter = input("Try to find a letter : ")


if letter in word :
	print("you found a correct letter")
else :
	print("this letter is not in the word")

