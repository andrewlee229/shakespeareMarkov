def grabPersonas():
	personas = []
	with open('../plays/macbeth.txt') as inputfile:
   		for line in inputfile:
   			#Skips blank lines
   			if len(line.strip()) != 0:
   				#Determines where the Dramatis Personae is located
	   			if(line.split()[0] == 'Dramatis'):
	   				#Skip blank line
	   				next(inputfile)
	   				nextLine = next(inputfile)
	   				#True until all persona are listed
	   				while(len(nextLine.strip()) != 0):
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

if __name__ == "__main__":
	personas = grabPersonas()
	print(personas)