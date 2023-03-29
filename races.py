import json
import requests
#immporting
class race:
    def __init__(self, raceRound, raceName, raceCircuit, raceDate, raceRestaurants, raceMap):
        self.raceRound = raceRound
        self.raceName = raceName
        self.raceCircuit = raceCircuit
        self.raceDate = raceDate
        self.raceRestaurants = raceRestaurants
        self.raceMap = raceMap
    
    def __dict__(self):
        return {
            "Round:" : self.raceRound,
            "Name:" : self.raceName,
            "Circuit:" : self.raceCircuit,
            "Date:" : self.raceDate,
            "Restaurants:" : self.raceRestaurants,
            "Map" : self.raceMap
            }
    #String method
    def __str__(self):
        return "{\n"f"round: {self.raceRound}\nname: {self.raceName}\ncircuit: {self.raceCircuit}\ndate: {self.raceDate}\nrestaurants: {self.raceRestaurants}\nmap: {self.raceMap}""},\n"
    #List method
    def __repr__(self):
        return f"round: {self.raceRound}\nname: {self.raceName}\ncircuit: {self.raceCircuit}\ndate: {self.raceDate}\nrestaurants: {self.raceRestaurants}\nmap: {self.raceMap}"
#Race class definition
rRetrieval = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/f8e2b420a8f9f5a27463eb29e1df63605822be13/races.json")
print(rRetrieval.status_code)
downloaded_list_races = rRetrieval.json()
#Request

race_list = []
#list definition
def assign_racedata():
    newRaceRound = ""
    newRaceName = ""
    newRaceCircuit = ""
    newRaceDate = ""
    newRaceRestaurants = ""
    newRaceMap = ""
    newRace = None
    for r in downloaded_list_races:
        newRaceRound = r['round']
        newRaceName = r['name']
        newRaceCircuit = r['circuit']
        newRaceDate = r['date']
        newRaceRestaurants = r['restaurants']
        newRaceMap = r['map']
        newRace = race(newRaceRound, newRaceName, newRaceCircuit, newRaceDate, newRaceRestaurants, newRaceMap)
        race_list.append(newRace)
#convert elements in downloaded list to objects and append to list
def save_racedata():    
    save_races_tofile = open("races.txt", "w")
    save_races_tofile.write("[")
    for r in race_list:
        save_races_tofile.write(r.__str__())
    save_races_tofile.write("]")
    save_races_tofile.close()
    #Write downloaded data to file
#save appended list of objects to file

assign_racedata()
save_racedata()

print (race_list)