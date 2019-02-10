# main pendu programme


import configdata as cd #import the config file
import fonctions as func #import the fonctions.py functions

print("Start of the game...")
user_name = input("Please enter your name")
print("Programme is choosing a word")
word = func.random_word()
print(word) # this line is only for test purpose !
display = ["*" for l in range(len(word))]
print("the word is : ", display)



while "*" in display and cd.try_nb > 0 :
	print("You have ",cd.try_nb,"tries to find the word")
	letter = input("Try to find a letter : ")
	# Add here later a check on the valid input

	if letter in word and len(letter)==1:
		print("You found a correct letter of the word")
		print(func.pos_letter(letter,word))
		for i in func.pos_letter(letter,word):
			display[i]=letter
		print("the word is now : ", display)

	elif len(letter)!=1:
		print("You can test only 1 letter at a time")
	else:
		print("This letter is not in the word :-(")
		print("Try again")
		cd.try_nb -=1 # reduce the number of try


if "*" not in display:
	print("Congratualtion, you found the word :-). You win ", cd.try_nb, " points")

else : 
	print("you didn't manage to find the word :(. You win 0 point.")


