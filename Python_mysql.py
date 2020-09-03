# MySQL CRUD with Python
# http://zetcode.com/db/mysqlpython/
# https://www.guru99.com/python-mysql-example.html

from errno import errorcode
import mysql.connector
import utils

def mysqlconnect():
    print("Trying to Connect.....")

    try:

        cnx = mysql.connector.connect(**utils.mysqlcred)
        cursor = cnx.cursor(buffered=True)
        ip = input("Enter any CRUD Operation add,upd,dlt,read : ")
        empID = '3'
        empNM = 'Select Stage 3'
        msg = "Started Operation...."
        print("Connection Established.....")

        if ip == "add":
            insrtqry = " INSERT INTO practice (STATUS_ID, STATUS_NAME) VALUES ('%s', '%s') " % (str(empID), str(empNM))
            cursor.execute(insrtqry)
            cnx.commit()
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
            cnx.commit()
            msg = "Data Updated Successfully"

        if ip == "dlt":
            dltqry = " DELETE from practice WHERE STATUS_ID=%s" % str(empID)
            cursor.execute(dltqry)
            cnx.commit()
            msg = "Data Deleted Successfully"

        cursor.close()
        cnx.close()
        return {"status": 200, "message": msg}

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return {"status": 400, "message": "Something is wrong with your user name or password"}
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return {"status": 400, "message": "Database does not exist"}
        else:
            return {"status": 400, "message": err}

print("\nMySQL Connection :",mysqlconnect())