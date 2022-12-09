from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# connecting to chinook database

db = create_engine("postgresql:///chinook")

meta =  MetaData(db)

# create variable for Artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key = True),
    Column("Name", String)
)

# Create album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key = True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key = True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key = False),
    Column("GenreId", Integer, primary_key = False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

with db.connect() as connection:
    # Query 1 select all from Artist table
    #select_query = artist_table.select()

    # Query 2 select only Name column from artist table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 select only Queen from artist table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 select only Id 51 from artist table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 select only artist id 51 from album table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 select only Queen as composer from track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
