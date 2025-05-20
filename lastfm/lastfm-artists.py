import requests
import mysql.connector
import lastfmapi as api

# import required information from config file
api_key = api.lastfm['api']
conn = mysql.connector.connect(
    host= api.mysql['host'],
    user= api.mysql['user'],
    password= api.mysql['password'],
    database=api.mysql['database']
)
cursor = conn.cursor()

# pull top 200 artists from lastfm api using params
top200 = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={api_key}&format=json&limit=200"
response = requests.get(top200)
data = response.json()

# extract artist names from json response
for artist in data['artists']['artist']:
    name = artist['name']
    playcount = int(artist['playcount'])
    listeners = int(artist['listeners'])
    url = artist['url']

# sql query to pull into database
# will update playcount and listeners if artist already exists
    sql = "INSERT INTO artists (name, playcount, listeners, url) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE playcount=VALUES(playcount), listeners=VALUES(listeners)"
    cursor.execute(sql, (name, playcount, listeners, url))

conn.commit()
cursor.close()
conn.close()

print("Artist DB update successful")
