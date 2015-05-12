import random

def grab_personas(play):
	personas = []
	with open('plays/' + play + '.txt') as inputfile:
   		for line in inputfile:
			#Determines where the Dramatis Personae is located
   			if(line.split()[0].lower() == 'dramatis'):
   				nextLine = next(inputfile)
   				#True until all persona are listed
   				while("<<" not in nextLine):
   					persona = nextLine.split()[0]
   					#If comma, it's a one word name
   					if ',' in persona:
   						persona = persona.replace(",","")
   					#If not, it's a two word name
   					else:
   						persona += " "
   						persona += nextLine.split()[1].replace(",","")
   					#Only major persona are in all caps
   					if persona.isupper():
   						personas.append(persona)
   					nextLine = next(inputfile)
   				return(personas)

def grab_lines(play, persona):
	lines = []
	#Stage directions that need to be excluded
	exclude = ['Exeunt', 'Re-enter', 'Enter', 'Exit', 'Enter,']
	#Whenever a persona appears in the play, it is with a period
	persona += "."
	with open('plays/' + play + '.txt') as inputfile:
		for line in inputfile:
			two_word_name = ""
			#Checks if the persona has a two word name
			try:
				two_word_name = line.split()[0] + " " + line.split()[1]
			except:
				two_word_name = ""
			#See if it is the beginning of a person's lines
			if(line.split()[0] == persona or two_word_name == persona):
				line = line.replace(persona, " ")
				line = line.replace("\n", "")
				lines.append(line)
				nextLine = next(inputfile)
				#Keep on grabbing lines until another person has a line
				while nextLine.split()[0] == "I" or not nextLine.split()[0].isupper():
					nextLine = nextLine.replace("\n", "")
					if nextLine.split()[0] not in exclude:
						lines.append(nextLine)
					nextLine = next(inputfile)
	return lines

def markov_set(lines):
	punct = [',','.',"\"","?","!",";",":","(",")"]
	mapping = {}
	for x in lines:
		line = x.split()
		prev_word = ""
		i = 0
		for l in line:
			#Remove punctuation and capitalization
			word = ''.join(ch for ch in l if ch not in punct)
			word = word.lower()
			if(word == "exit" or word == "exeunt"):
				break
			#Make I capitalized
			if(word == "i"):
				word = "I"
			#See if word has a dash in it
			try:
				if(word[len(word)-1] == "-"):
					word = word[:-1]
			except:
				pass
			#If beginning of line, just move on to next word
			if i == 0:
				i+=1
			#Assoicate current word with previous word
			else:
				if prev_word in mapping:
					mapping[prev_word].append(word)
				else:
					mapping.setdefault(prev_word,[]).append(word)
				#check if end of the line and if so reset
				if i == len:
					prev_word = ""
					break
			prev_word = word
	return(mapping)

def generate_text(mapping):
	x = 0
	#Get initial state
	state = random.choice(list(mapping.keys()))
	text = state.capitalize()
	state_values = mapping[state]
	state = random.choice(state_values)
	text = text + " " + state
	#While words is less than 25 in the setence continue
	while(x < 25):
		#If there isn't another state to transition to, break
		if state in mapping.keys():
			#Append word to setence
			state_values = mapping[state]
			state = random.choice(state_values)
			text = text + " " + state
			x+=1
		else:
			break
	text += "."
	#print(text)
	return text

def process_markov(play, persona):
	print("Play: " + play)
	print("Persona: " + persona)
	personas = grab_personas(play)
	lines = grab_lines(play, persona)
	mapping = markov_set(lines)
	return generate_text(mapping)