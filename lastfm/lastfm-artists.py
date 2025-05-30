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

# pull top 500 artists from lastfm api using params
top500 = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={api_key}&format=json&limit=500"
response = requests.get(top500)
data = response.json()

# extract artist names from json response
for artist in data['artists']['artist']:
    name = artist['name']
    playcount = int(artist['playcount'])
    listeners = int(artist['listeners'])
    url = artist['url']
    mbid = artist['mbid']
    
# sql query to pull into database
# will update playcount and listeners if artist already exists
# using mbid as primary key so will skip any blanks
    if not mbid.strip():
        continue
    sql = "INSERT INTO artists (name, playcount, listeners, url, mbid) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE playcount=VALUES(playcount), listeners=VALUES(listeners)"
    cursor.execute(sql, (name, playcount, listeners, url, mbid))

# pull albums using album API with artist mbid
    album_url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&mbid={mbid}&api_key={api_key}&format=json"
    album_response = requests.get(album_url)
    album_data = album_response.json()

    for album in album_data['topalbums']['album']:
        album_name = album['name']
        albumartist = album['artist']['name']
        album_playcount = int(album['playcount'])
        album_url = album['url']
        albumartist_mbid = album['artist']['mbid']

        albumsql = "INSERT INTO albums (name, artist, playcount, url, artistmbid) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE playcount=VALUES(playcount)"
        cursor.execute(albumsql, (album_name, albumartist, album_playcount, album_url, albumartist_mbid))

conn.commit()
cursor.close()
conn.close()
