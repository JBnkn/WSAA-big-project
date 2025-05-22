# Write a program that demonstrates that you understand creating and consuming RESTful APIs
# I will allow a lot of flexibility in this project, so that you can use it as an # opportunity to do something that is useful for your work.

# If you cannot think of a project to do: 
# Create a Web application in Flask that has a RESTful API, the application # should link to one or more database tables.
# You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from lastfmDAO import lastfmDAO

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return "Welcome to my REST server!"

@app.route('/hello/<name>')
def helloname(name):
        return f"Hello {name}, thanks for looking. I am building my REST server"

@app.route('/getartists', methods=['GET'])
def getartists():
        return jsonify(lastfmDAO.getallartists())

@app.route('/topalbums/<artist>', methods=['GET'])
def topalbums(artist):
        return jsonify(lastfmDAO.gettopalbums(artist))

@app.route('/createartist', methods=['POST'])
def createartist():
        jsonstring = request.json
        artist = {}
        if "name" not in jsonstring:
                abort(403)
        artist["name"] = jsonstring["name"]
        if "playcount" not in jsonstring:
                abort(403)
        artist["playcount"] = jsonstring["playcount"]
        if "listeners" not in jsonstring:
                abort(403)
        artist["listeners"] = jsonstring["listeners"]
        if "url" not in jsonstring:
                abort(403)
        artist["url"] = jsonstring["url"]  
        if "mbid" not in jsonstring:
                abort(403)
        artist["mbid"] = jsonstring["mbid"]      
        
        return jsonify(lastfmDAO.create(artist))

@app.route('/artist/<mbid>', methods=['PUT'])
def update(mbid):
        jsonstring = request.json
        artist = {}
        if "name" in jsonstring:
                artist["name"] = jsonstring["name"]
        if "playcount" in jsonstring:
                artist["playcount"] = jsonstring["playcount"]
        if "listeners" in jsonstring:
                artist["listeners"] = jsonstring["listeners"]  
        if "url" in jsonstring:
                artist["url"] = jsonstring["url"]
        if "mbid" in jsonstring:
                artist["mbid"] = jsonstring["mbid"]   
        return jsonify(lastfmDAO.update(mbid, artist))

@app.route('/deleteartist/<mbid>', methods=['DELETE'])
def deleteartist(mbid):
        artist_name = lastfmDAO.delete(mbid)
        return jsonify({ "message": f"Deleted {artist_name} from last.fm DB" })

if __name__ == "__main__":
    app.run(debug = True)