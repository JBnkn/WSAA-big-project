import mysql.connector
import config as cfg

class lastfmDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getallartists(self):
        cursor = self.getcursor()
        sql="select * from artists order by playcount desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToArtists(result))
        
        self.closeAll()
        return returnArray
    
    def gettopalbums(self, artist):
        cursor = self.getcursor()
        sql="select * from albums where artist = %s order by playcount desc limit 10"
        values = (artist,)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToAlbums(result))
        
        self.closeAll()
        return returnArray

    def create(self, artist):
        cursor = self.getcursor()
        sql="insert into artists (name, playcount, listeners, url, mbid) values (%s,%s,%s,%s,%s)"
        values = (artist.get("name"), artist.get("playcount"), artist.get("listeners"), artist.get("url"), artist.get("mbid"))
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return artist
    
    def update(self, mbid, artist):
        cursor = self.getcursor()
        sql="update artists set name= %s,playcount=%s, listeners=%s, url=%s where mbid = %s"
        values = (artist.get("name"), artist.get("playcount"), artist.get("listeners"), artist.get("url"), mbid)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, mbid):
        cursor = self.getcursor()
        sql1 = "select name from artists WHERE mbid = %s"
        cursor.execute(sql1, (mbid,))
        result = cursor.fetchone()
        artistname = result[0]
        sql2 = "delete from artists where mbid = %s"
        cursor.execute(sql2, (mbid,))
        self.connection.commit()
        self.closeAll()
        return artistname

    def convertToArtists(self, row):
        keys = ['name', 'playcount', 'listeners', 'url', 'mbid']
        return dict(zip(keys, row))
    
    def convertToAlbums(self, row):
        keys = ['id', 'name', 'artist', 'playcount', 'url', 'artistmbid']
        return dict(zip(keys, row))
    
lastfmDAO = lastfmDAO()