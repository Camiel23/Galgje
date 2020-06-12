import re
import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("intro-bericht")
print("het woord heeft " + str(lengtewoord) + " letters")