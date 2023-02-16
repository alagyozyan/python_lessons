#!/usr/bin/python3

################################################################################
## This program is something like an imitation of the game - 				  ##
## "Who Wants to be a Millionaire".											  ##
## Version - 0.0.1															  ##
################################################################################

################################################################################
## Import modules															  ##
################################################################################
import random
import os

################################################################################
## Defination of global Variables											  ##
################################################################################
QUESTIONS_FILE		= "questions_and_answers.txt"
TOP_SCORE_FILE		= "Top_scores.txt"
READ_FLAG			= "r"
WRITE_FLAG			= "w"
MAX_QUESTIONS_COUNT	= 10 
ANSWERS_LETTERS		= ['A', 'B', 'C', 'D']
ANSWERS				= ['YES', 'NO']
INPUT_MSG			= "\nEnter the correct answer letter: "
WRN_MSG				= "Please Enter only one of the following answers: "  
WRONG_ANSWER_MSG	= "\nYour answer is incorrect :(\nKeep trying"
RIGHT_ANSWER_MSG	= "\nCorrect ! Well done\n"
CORRECT_ANSWER 		= "The correct answer is : "
CA_MSG				= "Correct answers   -\t{}\t"
IA_MSG				= "Incorrect answers -\t{}\n"
Q_MSG				= "\nQuestion {}/{}\t"
TOTAL				= "\nTotal Questions   -\t{}"
R_MSG_1				= "\nGreat you have completed this quiz !\n"
R_MSG_2				= "Unfortunately You failed this quiz !\n"
R_MSG_3				= "Congratulations on your marvellous victory !\n"
R_MSG_4				= "Would you like to see the scores of all players ?\n"
R_MSG_5				= "Enter 'Yes' or 'No'... "
HEADER				= Q_MSG + CA_MSG + IA_MSG
QC 					= 0	# Count of questions
CC					= 0	# Count of Correct answers
IC					= 0	# Count of Incorrect answers 
			
################################################################################
## Open the file and return it's descriptor									  ##
################################################################################
def open_file (fn, m):
	if os.path.isfile(fn):
		return (open(fn, m))
	else:
		return (open(fn, 'a'))		

################################################################################
## Close the file															  ##
################################################################################
def close_file (fn):
	fn.close()
	return

################################################################################
## Read from the the specifed file and return it's content as a list		  ##
################################################################################
def get_file_content (fn, fd):
	if os.path.getsize(fn) != 0:
		return (fd.readlines())
	else:
		return None

################################################################################
## Return a random element from the given list								  ##
################################################################################
def get_random_line (lfl):
	return random.choice(lfl)

################################################################################
## Return question as a string froom the given line							  ##
################################################################################
def get_question (rl):
	return str(rl[0:rl.find('?')+1])

################################################################################
## Return asnwers as a list froom the given line							  ##
################################################################################
def get_answers (rl):
	return (rl[rl.find('?')+2:].split(' .'))

################################################################################
## Return the corrcet answer from the given lineas a string					  ##
## NOTE: Correct anwer always keeps in the first position	of the answers	  ##
################################################################################
def get_correct_answer (na):
	return str(na[0].strip("."))

################################################################################
## Remove one element of a list												  ##
################################################################################
def rm_list_element (lfl, rl):
	lfl.pop(lfl.index(rl))
	return

################################################################################
## Print next question from given line										  ##
################################################################################
def print_question (nq):
	print ("QUESTION: %s\n" % nq)
	return

################################################################################
## Reorganize the order of the given list items								  ##
################################################################################
def reorganize_answers_list (answers):
	random.shuffle(answers)
	return

################################################################################
## Returns a dictionary														  ##
## Keys		- letters (A: B: C: D:)											  ##
## Values  	- answers														  ##
################################################################################
def create_dict (answers):
	ad = {}
	for a, l in zip(answers, ANSWERS_LETTERS):
		ad.update({l:a.strip(".\n")})
	return ad

################################################################################
## Print answres in random order from given line							  ##
################################################################################
def print_answers (ad):
	for l, a in ad.items():
		print("%s: %s" % (l, a))
	return

################################################################################
## Ask Questions															  ##
################################################################################
def ask_questions (lfl):
	global QC
	global IC
	global CC
	while QC < MAX_QUESTIONS_COUNT :
		QC += 1
		random_line		= get_random_line		(lfl)
		next_question	= get_question			(random_line)
		next_answers	= get_answers			(random_line)
		correct_answer	= get_correct_answer	(next_answers)
	
		rm_list_element							(list_of_file_lines, random_line)
		os.system('clear')
		print (HEADER.format(QC, MAX_QUESTIONS_COUNT, CC, IC))
		print_question  						(next_question)
		reorganize_answers_list					(next_answers)
		answers_dict 	= create_dict			(next_answers)
		print_answers   						(answers_dict)
		answer_question (answers_dict, correct_answer)

################################################################################
## Function for entering player answers										  ##
################################################################################	
def answer_question (ad, ca):
	global IC
	global CC
	while True:
		player_answer = (input(INPUT_MSG)).upper()
		if player_answer not in ANSWERS_LETTERS:
			print (WRN_MSG, ANSWERS_LETTERS)
			continue
		elif ad[player_answer] == ca :
			os.system('clear')
			print_emoji(True)
			print (RIGHT_ANSWER_MSG)
			CC += 1
		else:
			print (WRONG_ANSWER_MSG)
			print_emoji(False)
			msg = list(ad.keys())[list(ad.values()).index(ca)]
			print (CORRECT_ANSWER, msg + ":", ca)
			IC += 1
		break
	input("\nPress 'Enter' to continue...")

################################################################################
## Function for Pritning emojis												  ##
################################################################################
def print_emoji (f):
	if f:
		print("\n###########################")
		print("###########################")
		print("####    ###########    ####")
		print("####    ###########    ####")
		print("###########################")
		print("###########################")
		print("###   ###############   ###")
		print("####   #############   ####")
		print("#####    #########    #####")
		print("#######             #######")
		print("###########################")
		print("###########################\n")
	else:
		print("\n###########################")
		print("###########################")
		print("####    ###########    ####")
		print("####    ###########    ####")
		print("###########################")
		print("###########################")
		print("#######             #######")
		print("#####    #########    #####")
		print("####   #############   ####")
		print("###   ###############   ###")
		print("###########################")
		print("###########################\n")

################################################################################
## Prints the result of the game											  ##
################################################################################
def print_results ():
	os.system('clear')
	print (R_MSG_1)
	if (QC // 2) > CC:
		print (R_MSG_2)
		print_emoji (False)
	else:
		print (R_MSG_3)
		print_emoji (True)
	print (CA_MSG.format(CC))
	print (IA_MSG.format(IC))
	print (TOTAL.format(QC))
	input("\nPress 'Enter' to continue...")
		 
################################################################################
## Get player credentials													  ##
################################################################################
def enter_player_name ():
	return (input ("Please enter your first name : "))
	
################################################################################
## Returns dictionary														  ##
## Keys   : Players' Names													  ##
## Values : Players' Scores													  ##
################################################################################
def get_players_dict (fc):
	pd = {}
	for el in fc:
		lfl = el.split("\t")
		if len(lfl) == 3 :
			pd.update({lfl[1]:(int(lfl[2].strip("\n")))})
		else :
			continue
	return pd

################################################################################
## Add or update current player and its score to the dict					  ##
################################################################################
def add_update_dict (pd, pn):
	if pn in pd.keys():
		pd[pn] += CC
	else :
		pd.update({pn:CC})
	return
	
################################################################################
## Returns Sorted dictionary by Values as a list of tuple					  ##
################################################################################
def sort_dict (pd):
	return (sorted(pd.items(), key=lambda x:x[1], reverse = True))

################################################################################
## Based on the results of the game, adds the full name of the player to the  ##
## corresponding line of the file.											  ##
################################################################################
def write_results (tfd, pl):
	i = 1 
	for el in pl:
		tfd.write(str(i)+".\t"+str(el[0]) + "\t" + str(el[1]) + "\n")
		i += 1

################################################################################
## Prints the players top scores read from appropriate file					  ##
################################################################################
def show_top_scores ():
	while True:
		os.system('clear')
		answer = (input(R_MSG_4 + R_MSG_5)).upper()
		if answer not in ANSWERS:
			print (WRN_MSG, ANSWERS)
			continue
		elif answer == ANSWERS[0] :
			os.system('clear')
			os.system('cat {}'.format(TOP_SCORE_FILE))
		break

################################################################################
## Main																		  ##
################################################################################
os.system('clear')
player_name			= enter_player_name	()

questions_fd		= open_file			(QUESTIONS_FILE, READ_FLAG)
list_of_file_lines	= get_file_content 	(QUESTIONS_FILE, questions_fd)
close_file								(questions_fd)
if list_of_file_lines == None:
	os.system('clear')
	print ("Please provede the '{}' file !".format(QUESTIONS_FILE))
	input ("Press 'Enter' to exit the game...")
	exit()

ask_questions 							(list_of_file_lines)
print_results							()

top_fd				= open_file			(TOP_SCORE_FILE, READ_FLAG)
file_content		= get_file_content	(TOP_SCORE_FILE, top_fd)
close_file								(top_fd)

players_list = []
if file_content != None:
	players_dict		= get_players_dict	(file_content)
	add_update_dict							(players_dict, player_name) 
	players_list		= sort_dict			(players_dict)
else:
	players_list		= [(player_name, CC)]

top_fd				= open_file			(TOP_SCORE_FILE, WRITE_FLAG)
write_results							(top_fd, players_list)
close_file								(top_fd)

show_top_scores							()
