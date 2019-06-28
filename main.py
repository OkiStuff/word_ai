from random import randint
import json
import placeholders as ph
# import

# Start Of Code
j = json.loads('{"letters":["A","a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t","U","u","V","v","W","w","X","x","Y", "y", "Z", "z"]}')
words = ph.null
words_correct = "ingore this,"
word_length = randint(0, 12)

correct = 0
number = 51
number_time = 0
letter_number = ph.null
word_ai = "..., "




def Letters():
	print(letter_number)

	if letter_number == 0:
		word_ai + word0
		word0 = (j[0])


	if letter_number == 1:
		word1 = (j[1])
		word_ai + word1
	if letter_number == 2:
		
		word2 = (j[2])
		word_ai + word2
	if letter_number == 3:
		
		word3 = (j[3])
		word_ai + word3
	if letter_number == 4:
		
		word4 = (j[4])
		word_ai + word4
	if letter_number == 5:
		
		word5 = (j[5])
		word_ai + word5
	if letter_number == 6:
		
		word6 = (j[6])
		word_ai + word6
	if letter_number == 7:
		
		word7 = (j[7])
		word_ai + word7

	if letter_number == 8:
		word8 = (j[8])
		word_ai + word8	
	if letter_number == 9:
		
		word9 = (j[9])
		word_ai + word9
	if letter_number == 10:
		
		word10 = (j[10])
		word_ai + word10
	if letter_number == 11:
		
		word11 = (j[11])
		word_ai + word11

	if letter_number == 12:
		
		word12 =(j[12])
		word_ai + word12

	if letter_number == 13:
		
		word13 =(j[13])
		word_ai + word13

	if letter_number == 14:
			
		word14 = (j[14])
		word_ai + word14
	if letter_number == 15:
		
		word15 = (j[15])
		word_ai + word15
	if letter_number == 16:
		
		word16 = (j[16])
		word_ai + word16
	if letter_number == 17:
		
		word17 = (j[17])
		word_ai + word17
	if letter_number == 18:
		word18 = (j[18])
		word_ai + word18

	if letter_number == 19:
		
		word19 = (j[19])
		word_ai + word19
	if letter_number == 20:
		
		word20 = (j[20])
		word_ai + word20
	if letter_number == 21:
		
		word21 = (j[21])
		word_ai + word21
	if letter_number == 22:
		
		word22 = (j[22])
		word_ai + word22
	if letter_number == 23:
		word23 = (j[23])
		word_ai + word23
	if letter_number == 24:
		word24 = (j[24])
		word_ai + word24
		
	if letter_number == 25:
		word_ai + word25
		word25 = (j[25])
	if letter_number == 26:
		word_ai + word26
		word26 = (j[26])
	if letter_number == 27:
		word_ai + word27
		word27 = (j[27])
	if letter_number == 28:
		word_ai + word28
		word28 = (j[28])
	if letter_number == 29:
		word_ai + word29
		word29 = (j[29])
	if letter_number == 30:
		word_ai + word30
		word30 = (j[30])
	if letter_number == 31:
		word_ai + word31
		word31 = (j[31])
	if letter_number == 32:
		word_ai + word32
		word32 = (j[32])
	if letter_number == 33:
		word_ai + word33
		word33 = (j[33])
	if letter_number == 34:
		word_ai + word34
		word34 = (j[34])
	if letter_number == 35:
		word_ai + word35
		word35 = (j[35])
	if letter_number == 36:
		word_ai + word36
		word36 = (j[36])
	if letter_number == 37:
		word37 = (j[37])
		word_ai + word37
	if letter_number == 38:
		word_ai + word38
		word38 = (j[38])
	if letter_number == 39:
		word_ai + word39
		word39 = (j[39])
	if letter_number == 40:
		word_ai + word40
		word40 = (j[40])
	if letter_number == 41:
		word_ai + word41
		word41 = (j[41])
	if letter_number == 42:
		word_ai + word42
		word42 = (j[42])
	if letter_number == 43:
		word43 = (j[43])
		word_ai + word43
	if letter_number == 44:
		word_ai + word44
		word44 = (j[44])
	if letter_number == 45:
		word45 = (j[45])
		word_ai + word45
		
	if letter_number == 46:
		word_ai + word46
		word46 = (j[46])
	if letter_number == 47:
		word_ai + word47
		word47 = (j[47])

	if letter_number == 48:
		word_ai + word48
		word48 = (j[48])

	if letter_number == 49:
		word_ai + word49
		word49 = (j[49])

	if letter_number == 50:
		word_ai + word50
		word50 = (j[50])

	if letter_number == 51:
		word_ai + word51
		word51 = (j[51])
	print(word_ai)
def machine_learning():
	question = input("Was this a word? Y/N")
	if question == "Y":
		print("Thanks for the feedback.")
		correct + 1
	if question == "N":
		print("Thanks. I'll try to get better!")
	elif question == "y":
		print("Thanks for the feedback.")
	elif question == "n":
		print("Thanks. I'll try to get better!")
	else:
		print("That wasn't Y/N! Try Again")
		try_again()



def try_again():
	machine_learning()
print(word_ai)

while number_time < word_length:
	letter_number = randint(0,51)
	number_time + 1
	Letters()
	machine_learning()
