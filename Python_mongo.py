# MongoDB CRUD with Python
# https://university.mongodb.com/courses/M220P/about
# https://www.geeksforgeeks.org/mongodb-and-python/

import pymongo
import utils

def mongoconnect():
    print("Trying to Connect.....")

    try:

        myClient = pymongo.MongoClient(utils.mongocred)
        mydb = myClient[utils.mongodatabase]
        mycol = mydb[utils.mongocollection]
        print("Connection Established.....")

        print(mydb.collection_names())
        print(mycol)

        ip = input("Enter any CRUD Operation add,upd,dlt,read : ")
        empID = '113959'
        empNM = 'oj'
        msg = "Started Operation...."

        if ip == "add":
            mycol.insert_one({"emp_id": int(empID), "emp_name": str(empNM)})
            msg = "Data Inserted Successfully"

        if ip == "read":
            readqry = mycol.find_one({"emp_id": str(empID)})
            print(readqry)
            msg = "Data Retrieved Successfully"

        if ip == "upd":
            data = {"emp_name" : "Python_OJ"}
            key = {'emp_id' : empID}
            mycol.update_one(key, {'$set': data}, upsert=True)
            msg = "Data Updated Successfully"

        if ip == "dlt":
            mycol.delete_one({"emp_id": int(empID)})
            msg = "Data Deleted Successfully"

        myClient.close()
        return {"status": 200, "message": msg}

    except pymongo.errors.ConnectionFailure as e:
        return {"message": "Internal server error %s" % e, "status": 500}

print("\nMongo Connection :",mongoconnect())