from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based mode for "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)

# create a class-based mode for "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based mode for "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# create a new instance of "sessionmaker"
Session = sessionmaker(db)

# open a actual session
session  = Session()

# create the database usin declarative_base subcalss
base.metadata.create_all(db)

# Query 1 select all from "Artist table"
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep = " | ")

# Query 2 select only "Queen" from "Artist" table
# artist = session.query(Artist).filter_by(Name = "Queen").first()
# print(artist.ArtistId, artist.Name, sep = " | ")

# Query 3 select only "ArtistId" 51 from "Artist" table
# artist = session.query(Artist).filter_by(ArtistId = 51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 select Albums from Album table with ArtistId 51
# albums = session.query(Album).filter_by(ArtistId = 51)
# for album in albums:
#     print(
#         album.AlbumId,
#         album.Title,
#         album.ArtistId,
#         sep=" | "
#     )

# Query 5 select tracks from Track table with Composer Queen
tracks = session.query(Track).filter_by(Composer = "Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.Composer, track.UnitPrice, sep=" | ")
