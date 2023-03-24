import json
import requests

class constructores():
    def __init__(self, constName, team, nationality, driverID):
        self.constName = constName
        self.team = team
        self.nationality = nationality 
        self.driverID = driverID
    
    def dict(self):
        return {'name': self.constName,
                'team': self.team,
                'nationality': self.nationality}

url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json"
args = {"id": "string",
        "name": "string",
        "nationality": "string"
}
response = requests.get(url, args)
if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
    print(data[0])    
    print(data[0]['id'])
else:
    print("An error ocurred.")

print(url.status_code)
textoDescargado = url.json()
print(textoDescargado)

constructorfile = open("contructorfile.txt", "w")
constructorfile.write(str(textoDescargado))
constructorfile.close()   