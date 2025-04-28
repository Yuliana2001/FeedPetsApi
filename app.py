from flask import Flask, jsonify, request #convierte un objeto a json
app = Flask(__name__)
from pets import pets

#ruta de prueca
@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})


@app.route('/pets', methods=['GET'])
def get_pets():
    return jsonify({"pets":pets, "message":"mascotas"})


#quiero buscar por especie
@app.route('/pets/<string:especie>', methods=['GET'])
def getEspecie(especie):
    PetsFound = [pet for pet in pets if pet['especie']== especie]
    if (len(PetsFound)>0):
        return jsonify({"mascota":PetsFound[1]})
    return jsonify({"message":"no hay mascotas de esa especie"})


@app.route('/pets', methods=['POST'])
def addPets():
    newPet = {
        "nombre":request.json['nombre'],
        "raza":request.json['raza'],
        "especie":request.json['especie'],
        "sexo":request.json['sexo'],
        "edad": int(request.json['edad']),
        "peso":int(request.json['peso']),
    }
    pets.append(newPet)
    return jsonify({"message":"Mascota agregada", "mascotas":pets})

@app.route('/pets/<string:nombre>', methods=['PUT'])
def updatePet(nombre):
    petFoundByName = [pet for pet in pets if pet['nombre']==nombre]
    if (len(petFoundByName)>0):
            petFoundByName[0]['raza']=request.json['raza']
            petFoundByName[0]['especie']=request.json['especie']
            petFoundByName[0]['sexo']=request.json['sexo']
            petFoundByName[0]['edad']=int(request.json['edad'])
            petFoundByName[0]['peso']=int(request.json['peso'])
            return jsonify({"message":"Mascota actualizada", "mascotas":petFoundByName[0]})

@app.route('/pets/<string:nombre>', methods=['DELETE'])
def deletePet(nombre):
    petFoundByName = [pet for pet in pets if pet['nombre']==nombre]
    if (len(petFoundByName)>0):
        pets.remove(petFoundByName[0])
        return jsonify({"message":"Mascota eliminada", "mascotas":pets})
    return jsonify({"message":"no se encontró mascota con ese nombre"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True) #incializar y cuando se haga un cambio, se vuelva a iniciar
    