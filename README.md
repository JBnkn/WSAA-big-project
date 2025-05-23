# Last.fm Database Interface
**by Joseph Benkanoun**

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Lastfm_logo.svg" alt="LastFM Logo" width="400"/>

This repository contains my big project for the 2025 [Web Services and Applications](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=Web%20Services%20and%20Applications) module as part of the [Higher Diploma in Science in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics) at ATU.

### Module Description

> An introduction to and overview of web applications and services – accessing and consuming them and their common architectures.

### Learning Outcomes

> Describe common architectures of web services and web applications.

> Create a simple web service.

> Programmatically access a web service.

> Construct a data set by querying a web service.

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


## MySQL Configuration
To ensure data is pulled into MySQL from the last.fm API correctly, you can create the relevant tables in your database using the code below:

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


## API Endpoints

## Potential Improvements
- automate monthly pull from last.fm API using cron to update top artists / playcounts / listeners
- pull top albums from last.fm API when user adds new artist
- add CRUD functionality around album DB

## References
- https://www.youtube.com/watch?v=AgVqsmz-ZW4
- https://www.youtube.com/watch?v=F7AK-WzpYdY
- https://www.last.fm/api/intro
- https://www.youtube.com/watch?v=KjNXOi4Wqbk
- https://www.youtube.com/watch?v=ru_YWeOh2kU
- https://www.w3schools.com/js/js_ajax_intro.asp