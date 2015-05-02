from random import randint

def grab_personas():
	personas = []
	with open('../plays/macbeth.txt') as inputfile:
   		for line in inputfile:
			#Determines where the Dramatis Personae is located
   			if(line.split()[0] == 'Dramatis'):
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

def grab_lines(persona):
	lines = []
	#Whenever a persona appears in the play, it is with a period
	persona += "."
	with open('../plays/macbeth.txt') as inputfile:
		for line in inputfile:
			if(line.split()[0] == persona):
				line = line.replace(persona, " ")
				line = line.replace("\n", "")
				lines.append(line)
				print(line)
				nextLine = next(inputfile)
				while nextLine.split()[0] == "I" or not nextLine.split()[0].isupper():
					nextLine = nextLine.replace("\n", "")
					lines.append(nextLine)
					print(nextLine)
					nextLine = next(inputfile)
	return lines

def markov_set(lines):
	punct = [',','.',"\"","?","!",";"]
	mapping = {}
	for x in lines:
		line = x.split()
		prev_word = ""
		i = 0
		for l in line:
			word = ''.join(ch for ch in l if ch not in punct).lower()
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
	size = len(mapping)
	state = randint(0,size)
	print(state)
	x = 0
	while(x < 25):
		word = state
		x+=1

if __name__ == "__main__":
	personas = grab_personas()
	#print(personas)
	lines = grab_lines("MACBETH")
	mapping = markov_set(lines)
	for k,v in markov_set(lines).items():
		print(k + str(v))
	generate_text(mapping)