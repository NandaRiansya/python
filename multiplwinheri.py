class team :
    def setTeam(self,team):
        self.team = team
    
    def showTeam(self):
        print(self.team)

class tipe_hero:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(team,tipe_hero):

    def __init__(self,name,health):
        self.name = name
        self.health = health

Ucup = Hero ('Ucup',100)
Ucup.setTeam("merah")
Ucup.setTipe("cundang")

Ucup.showTeam()
Ucup.showTipe()