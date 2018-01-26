f = open('aliens.csv')
aliens = f.readlines()
aliensList = []
planetsList = list()
header = True
for line in aliens:
    if not header:
        alien = line.split(",")[0]
        planet = line.split(",")[1].replace("\n","")
        aliensList.append(alien)
        planetsList.append(planet)
    else:
        header = False

output = open('planets.csv',mode="w")
output.write("species,planet\n")

planet_zerg = []
planet_ho = []
planet_mars = []

for alien in aliensList:
    planet = planetsList[aliensList.index(alien)]
    if planet==" zerg-1":
        planet_zerg.append(alien)
    if planet==" ho":
        planet_ho.append(alien)
    if planet==" mars":
        planet_mars.append(alien)


class Zergalizer:
    def do_zergalization(self, species):
        transformed = list()
        for s in species:
            transformed.append(s.upper())
        output.write(" ".join(transformed)+",zerg"+"\n")

class Hoizer:
    def do_hoizification(self, species):
        transformed = list()
        for s in species:
            transformed.append(s+"HO!")
        output.write((" | ").join(transformed)+",ho"+"\n")

class Marsianizer:
    def do_marsianization(self, species):
        transformed = list()
        for s in species:
            transformed.append(" ".join(s.split("."))+"m")
        output.write((" ~~ ").join(transformed)+",mars"+"\n")

Zergalizer().do_zergalization(planet_zerg)
Hoizer().do_hoizification(planet_ho)
Marsianizer().do_marsianization(planet_mars)