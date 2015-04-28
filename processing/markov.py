def grabPersonas():
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

def grabLines(persona):
	lines = []
	#Whenever a persona appears in the play, it is with a period
	persona += "."
	with open('../plays/macbeth.txt') as inputfile:
		for line in inputfile:
			if(line.split()[0] == persona):
				line = line.replace(persona, " ")
				line = line.replace("\n", "")
				lines.append(line)
				nextLine = next(inputfile)
				while nextLine.split()[0] == "I" or not nextLine.split()[0].isupper():
					nextLine = next(inputfile)
					nextLine = nextLine.replace("\n","")
					lines.append(nextLine)
	return lines
if __name__ == "__main__":
	personas = grabPersonas()
	print(personas)
	print(grabLines("MACBETH"))