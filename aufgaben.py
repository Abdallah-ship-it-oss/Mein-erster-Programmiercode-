
#Das ist mein dritter Programmcode.

aufgaben = ["Deutschlernen", "Fitnessstodio","Programmieren"]

#Eingabe eines dringenden auftrags.

dringende_aufgabe = "Das Gebet"
aufgaben.insert(0,dringende_aufgabe)

#neue aufgeben eingeben.

neue_aufgabe = "schlafen"
aufgaben.append(neue_aufgabe)
print(len(aufgaben))

#aufgaben löschen.

abgeschlossen = aufgaben.pop (2)
print(abgeschlossen)

#suchen.

pos = aufgaben.index("Programmieren")
print(pos)

print(aufgaben)

