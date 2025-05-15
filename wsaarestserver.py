# Write a program that demonstrates that you understand creating and consuming RESTful APIs
# I will allow a lot of flexibility in this project, so that you can use it as an # opportunity to do something that is useful for your work.

# If you cannot think of a project to do: 
# Create a Web application in Flask that has a RESTful API, the application # should link to one or more database tables.
# You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"