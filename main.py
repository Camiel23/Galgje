import re
import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Hallo, welkom bij galgje! Raad letters en als je het hele woord weet, typ het woord helemaal om te winnen. Succes en veel plezier!")
print("het woord heeft " + str(lengtewoord) + " letters")


guesses = ""

turns = 5

while turns > 0:
  verkeerd = 0
  for letter in woord:
      if letter in guess:
        print (letter)
      else: 
        print("_")
        verkeerd = verkeerd + 1
  if failed == 0:
    print("Gefeliciteerd, je hebt in" + str(guesses) + "gewonnen!")
  guess = input("Raad een letter: ")
  guesses = guesses + guess
  if guess not in woord:
    turns = turns - 1
    print("Jammer, fout...")
    print("Je hebt nog" + turns + "gokkansen over")
    
    if turns == 5:
      print ("_________")
      print ("|	 |")
      print ("|	 O")
      print ("|")
      print ("|")
      print ("|")
      print ("|________")
    if turns == 4:
      print ("_________")
	    print ("|  |")
	    print ("|	 O")
	    print ("|	 |")
	    print ("|	 |")
	    print ("|")
	    print ("|________")

    if turns == 3:
    	print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\|")
  		print ("|	 |")
			print ("|")
			print ("|________")

    if turns == 2:
    	print ("_________")
    	print ("|	 |")
			print ("|	 O")
			print ("|	\|/")
			print ("|	 |")
			print ("|")
			print ("|________")

    if turns == 1:
      print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\|/")
			print ("|	 |")
			print ("|	/ ")
			print ("|________")

    if turns == 0:
      print ("_________")
			print ("|	 |")
			print ("|	 O")
			print ("|	\|/")
			print ("|	 |")
			print ("|	/ \ ")
			print ("|________") 
      print("Helaas, je hebt verloren. Het woord was:" + woord )

