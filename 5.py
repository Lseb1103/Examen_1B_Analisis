import pymysql

# Abre conexion con la base de datos
db = pymysql.connect("localhost","luisseb","st11032014","tiktokconcet")
##################################################

# procesa una unica linea usando el metodo fetchone().
data = cursor.fetchone()
print ("Database version : {0}".format(data))


# Open database connection
db = pymysql.connect("localhost","luisseb","st11032014","tiktokconcet")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


# desconecta del servidor
db.close()