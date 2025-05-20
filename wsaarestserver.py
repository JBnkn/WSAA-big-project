# Write a program that demonstrates that you understand creating and consuming RESTful APIs
# I will allow a lot of flexibility in this project, so that you can use it as an # opportunity to do something that is useful for your work.

# If you cannot think of a project to do: 
# Create a Web application in Flask that has a RESTful API, the application # should link to one or more database tables.
# You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.

from flask import Flask, request, jsonify, abort
from lastfmDAO import lastfmDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Welcome to my REST server!"

@app.route('/hello/<name>')
def helloname(name):
        return f"Hello {name}, thanks for looking. I am building my REST server"

@app.route('/getartists', methods=['GET'])
def getartists():
        return jsonify(lastfmDAO.getallartists())

@app.route('/getalbums', methods=['GET'])
def getalbums():
        return jsonify(lastfmDAO.getallalbums())

@app.route('/topalbums/<artist>', methods=['GET'])
def topalbums(artist):
        return jsonify(lastfmDAO.gettopalbums(artist))

if __name__ == "__main__":
    app.run(debug = True)