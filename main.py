import re
import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Hallo, welkom bij galgje! Raad letters en als je het hele woord weet, typ het woord helemaal om te winnen. Succes en veel plezier!")
print("het woord heeft " + str(lengtewoord) + " letters")

while True: #woord wordt geraden
  userguess = (input(": "))
  match = re.search(userguess, woord)
  if userguess == woord
    print("je hebt het woord" + "'" + woord = "'" + "geraden")
    break
  
  

