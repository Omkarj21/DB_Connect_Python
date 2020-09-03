# PostgreSQL CRUD with Python
# https://www.postgresqltutorial.com/postgresql-python/
# https://pynative.com/python-postgresql-tutorial/

import psycopg2
import sshtunnel
import utils

connection = None
sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def postgreconnect():
    print("Trying to Connect.....")

    try:

        with sshtunnel.SSHTunnelForwarder((utils.postgres["ip"], utils.postgres["port"]),ssh_username=utils.postgres["user"], ssh_password=utils.postgres["pwd"], remote_bind_address=(utils.postgres["host"],utils.postgres["postgrsport"])) as tunnel:
            print("Server Connected.....")

            connection = psycopg2.connect(
                user=utils.postgres["postgrsusr"], password=utils.postgres["postgrspwd"],
                host=utils.postgres["host"], port=tunnel.local_bind_port,
                database=utils.postgres["postgrsdb"],
            )
            print("Database Connected.....")

            cursor = connection.cursor()

            ip = input("Enter any CRUD Operation add,upd,dlt,read : ")
            empID = '3'
            empNM = 'Select Stage 3'
            msg = "Started Operation...."

            if ip == "add":
                insrtqry = " INSERT INTO practice (STATUS_ID, STATUS_NAME) VALUES ('%s', '%s') " % (
                str(empID), str(empNM))
                cursor.execute(insrtqry)
                connection.commit()
                msg = "Data Inserted Successfully"

            if ip == "read":
                viewqry = "SELECT * FROM practice WHERE STATUS_ID=%d" % int(empID)
                cursor.execute(viewqry)
                allrecords = cursor.fetchall()
                print(allrecords)
                msg = "Data Retrieved Successfully"

            if ip == "upd":
                updqry = " UPDATE practice SET STATUS_NAME = '%s' WHERE STATUS_ID = '%s' " % (str(empNM), int(empID))
                cursor.execute(updqry)
                cursor.commit()
                msg = "Data Updated Successfully"

            if ip == "dlt":
                dltqry = " DELETE from practice WHERE STATUS_ID=%s" % str(empID)
                cursor.execute(dltqry)
                cursor.commit()
                msg = "Data Deleted Successfully"


    except(Exception, psycopg2.Error, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)
        return {"status": 400, "message": error}

    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL Connection is Closed")
            return {"status": 200, "message": msg}

print("\nPostgreSQL Connection :",postgreconnect())