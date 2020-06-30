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
  guess = input("Raad een letter: ")
  
  for letter in woord:
      if letter in guess:
        print (letter)
      else: 
        print("-")
        verkeerd = verkeerd + 1
  
  if verkeerd == 0:
    print("Gefeliciteerd, je hebt gewonnen!")
    break
  
  guesses = guesses + guess
  if guess not in woord:
    turns = turns - 1
    print("Jammer, fout...")
    print("Je hebt nog " + str(turns) + " gokkansen over")
    
    if turns == 0:
      print("Helaas, je hebt verloren. Het woord was: " + woord )

