import random, os

def grab_personas(play):
	personas = []
	#opens file on local computer
	#with open('../plays/' + play + '.txt') as inputfile:
	#opens file on server
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
	exclude = ['Exeunt', 'Re-enter', 'Enter', 'Exit', 'Enter,']
	#Whenever a persona appears in the play, it is with a period
	persona += "."
	with open('plays/' + play + '.txt') as inputfile:
		for line in inputfile:
			two_word_name = ""
			try:
				two_word_name = line.split()[0] + " " + line.split()[1]
			except:
				two_word_name = ""
			if(line.split()[0] == persona or two_word_name == persona):
				line = line.replace(persona, " ")
				line = line.replace("\n", "")
				lines.append(line)
				#print(line)
				nextLine = next(inputfile)
				while nextLine.split()[0] == "I" or not nextLine.split()[0].isupper():
					nextLine = nextLine.replace("\n", "")
					if nextLine.split()[0] not in exclude:
						lines.append(nextLine)
						#print(nextLine)
					#print(nextLine)
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
			word = ''.join(ch for ch in l if ch not in punct)
			word = word.lower()
			if(word == "exit" or word == "exeunt"):
				break
			if(word == "i"):
				word = "I"
			try:
				if(word[len(word)-1] == "-"):
					word = word[:-1]
			except:
				pass
			if i == 0:
				i+=1
			elif i == len:
				prev_word = ""
				break
			else:
				if prev_word in mapping:
					mapping[prev_word].append(word)
				else:
					mapping.setdefault(prev_word,[]).append(word)
			prev_word = word
	return(mapping)

def generate_text(mapping):
	x = 0
	text = ""
	size = len(mapping)
	state = random.choice(list(mapping.keys()))
	text = state.capitalize()
	state_values = mapping[state]
	state = random.choice(state_values)
	text = text + " " + state
	while(x < 25):
		if state in mapping.keys():
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
	#print(personas)
	lines = grab_lines(play, persona)
	mapping = markov_set(lines)
	#for k,v in markov_set(lines).items():
	#	print(k + str(v))
	return generate_text(mapping)