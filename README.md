# Last.fm Database Interface
**by Joseph Benkanoun**

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Lastfm_logo.svg" alt="LastFM Logo" width="400"/>

This repository contains my big project for the 2025 [Web Services and Applications](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=Web%20Services%20and%20Applications) module as part of the [Higher Diploma in Science in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics) at ATU.

### Module Description

> An introduction to and overview of web applications and services – accessing and consuming them and their common architectures.

### Learning Outcomes

- Describe common architectures of web services and web applications.
- Create a simple web service.
- Programmatically access a web service.
- Construct a data set by querying a web service.

## Project Description
[Last.fm](https://www.last.fm/) is a popular online music website that tracks people's song listening habits. Founded in (2002 before the rise on online music streaming), users could initially download a plug-in that would connect to a music playing tool such as iTunes, which would then feed their plays to their last.fm user account, allowing them to see their top artists and listening trends.

For this project, I decided to utilise the [last.fm API](https://www.last.fm/api) to download the top artists and their albums into a local MySQL database. I then used that database to build out my Flask server and DAO to create an interactive page where users can see the current top artists in one place, and review their most popular albums. The interface also allows for creating, updating, and deleting artists to showcase a range of CRUD operations.

## Repository Structure
``` bash
WSAA-big-project/
├── lastfm/
│   └── lastfm-artists.py    # pulls data from last.fm API to local MySQL database
├── .gitignore               # Git exclusions (incl config files)
├── README.md                # project outline
├── index.html               # HTML and AJAX interfact
├── lastfmDAO.py             # Database Access Object - functions to call from MySQL DB
└── wsaarestserver.py        # RESTful API server - Flask functions
```

## Requirements
This project used the following Python libraries:

- [Flask](https://flask.palletsprojects.com/en/stable/): framework to create REST API
- [Flask CORS](https://pypi.org/project/flask-cors/): enables sharing to frontend
- [MySQL Connector](https://www.mysql.com/products/connector/): connects to MySQL database

## MySQL Configuration
To ensure data is pulled into MySQL from the last.fm API correctly (having registered an API account with them), you can create the relevant tables in your database using the code below:

### Artists
``` bash
CREATE TABLE artists (
    name VARCHAR(255),
    playcount BIGINT,
    listeners INT,
    url VARCHAR(500),
    mbid VARCHAR(36) PRIMARY KEY
);
```

- <b>name: </b> Artist Name
- <b>playcount: </b> Total Number of Plays for Artist
- <b>listeners: </b> Total Number of Listeners for Artist
- <b>url: </b> Link to Artist's Last.fm Profile
- <b>mbid: </b> [MusicBrainz Identifier](https://musicbrainz.org/), a unique code for each artist

### Albums
``` bash
CREATE TABLE albums (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    artist VARCHAR(255),
    playcount INT,
    url VARCHAR(500),
    artistmbid VARCHAR(36),
    FOREIGN KEY (artistmbid) REFERENCES artists(mbid)
);
```
- <b>id: </b> Primary Key for Table
- <b>name: </b> Album Name
- <b>artist: </b> Album Artist
- <b>playcount: </b> Total Number of Plays for Album
- <b>url: </b> Link to Album's Last.fm Profile
- <b>artist mbid: </b> Artist [MusicBrainz Identifier](https://musicbrainz.org/), serves as Foreign Key to connect tables

## API Endpoints

- <code>GET /getartists</code>: fetches a list of all artists from the database, ordered by descending playcount
- <code>POST /createartist</code>: creates a new artist using JSON
- <code>PUT /artist/\<mbid></code>: updates an existing artist using JSON, requires their unique mbid
- <code>DELETE /deleteartist/\<mbid></code>: deletes an existing artist, requires their unique mbid
- <code>GET /topalbums/\<artist></code>: fetches the top 10 albums for specified artist, ordered by descending playcount 

## Potential Improvements
- Automation: I could implement a scheduled task using <code>cron</code> to automatically retrieve and update top artists, playcounts, and listener data from the Last.fm API on a monthly basis without need for running <code>lastfm-artists.py</code> manually.
- I could improve the system to automatically call the Last.fm API and retrieve the top albums for an artist whenever a new artist is added to the database manually by the user (as present this is only occuring as part of the total call to the Last.fm API).
- This system currently only has CRUD functionality for the Artists DB - I could widen the scope to add these functions for the Albums DB.

## References
- [A brief Introduction to Flask (Python Web Framework) - A Byte of Code](https://www.youtube.com/watch?v=AgVqsmz-ZW4)
- [A brilliant introduction to Flask - Pythonist](https://www.youtube.com/watch?v=F7AK-WzpYdY)
- [Last.fm API Documentation](https://www.last.fm/api/intro)
- [Consuming REST Web Service in an HTML Page - ChargeAhead](https://www.youtube.com/watch?v=KjNXOi4Wqbk)
- [JSON Response To HTML Table | Javascript (Ajax) - Dennis Ivy](https://www.youtube.com/watch?v=ru_YWeOh2kU)
- [AJAX Introduction - W3Schools](https://www.w3schools.com/js/js_ajax_intro.asp)
- [ChatGPT](https://chat.openai.com/): I used ChatGPT for assistance when I encountered a chunk of code that simply wouldn't work for me, and also to simplify error messages that I couldn't quite decode the documentation for. A key area I had a challenge with was connecting the backend to the frontend, and ChatGPT was useful at breaking down the steps for me to stitch the whole project together.