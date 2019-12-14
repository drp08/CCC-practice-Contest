# apple scorings input
def game():
	threesapple = input()
	twosapple = input()
	onesapple = input()

# banana scorings input

	threesbanana = input()
	twosbanana = input()
	onesbanana = input()
 # if statements to check if each number 
	if threesapple == int:
		pass
	elif threesapple != int:
		threesapple = input()

	if twosapple == int:
		pass
	elif twosapple != int:
		twosapple = input()

	if onesapple == int:
		pass
	elif onesapple != int:
		onesapple = input()

	if threesbanana == int:
		pass
	elif threesbanana != int:
		threesbanana = input()

	if twosbanana == int:
		pass
	elif twosbanana != int:
		twosbanana = input()

	if onesbanana == int:
		pass
	else:
		onesapple = input()



# total banana scorings 
	applesScore = (threesapple *3) + (twosapple * 2) + (onesapple * 1)

	bananasScore = (threesbanana *3) + (twosbanana * 2) + (onesbanana * 1)



# checking who won
	if applesScore > bananasScore:
 		print('a')

	elif applesScore < bananasScore:
		print('b')

	else:
		print('t')

game()