import psycopg2


# connect to chinook
connection = psycopg2.connect(database = "chinook")

# build a cursor for the database
cursor = connection.cursor()

# Query 1
# cursor.execute('SELECT * FROM "Artist"')

# Query 2
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# Query 3
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# fetch multiple results
results = cursor.fetchall()

# fetch single result
#results = cursor.fetchone()

# close connection
connection.close()

# print results
for item in results:
    print(item)
