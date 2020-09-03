# Mongo DB ==>
# In Below Replace "MONGO_USER, MONGO_PASSWORD, MONGO_IP, MONGO_DATABASE, MONGO_COLLECTION" with Your DB Details
mongocred = "mongodb://MONGO_USER:MONGO_PASSWORD@MONGO_IP:27017/?authSource=MONGO_DATABASE"
mongodatabase = "MONGO_DATABASE"
mongocollection = "MONGO_COLLECTION"
# --------------------------------------------------------------------------------------------------------

# MySQL DB ==>
# In Below Replace "MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASSWORD" with Your DB Details
mysqlcred = {"host" : "MYSQL_HOST","db" : "MYSQL_DB","user" : "MYSQL_USER","password" : "MYSQL_PASSWORD"}
# --------------------------------------------------------------------------------------------------------

# PostgreSQL DB ==>
# In Below Replace "HOST_IP, HOST_USER, HOST_PASSWORD, PostgreSQL_USER, PostgreSQL_PASSWORD, PostgreSQL_DATABASE" with Your DB Details
postgres = {"ip":'HOST_IP',"port":22,"user":'HOST_USER',"pwd":'HOST_PASSWORD',
            "host":'127.0.0.1',"postgrsport":5432,
            "postgrsusr":'PostgreSQL_USER',"postgrspwd":'PostgreSQL_PASSWORD',"postgrsdb":'PostgreSQL_DATABASE'}
# --------------------------------------------------------------------------------------------------------