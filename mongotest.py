import  pymongo
client = pymongo.MongoClient("mongodb+srv://saurabhdata:Rajbhatta1!#$@saurabhdata.ckhjdot.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "saurabh",
    "last name " : "kumar",
    "mobile_no" : 766581990
}
d = {
    "name" : "saurabh",
    "last name " : "kumar",
    "mobile_no" : 766581990
}
d = {
    "name" : "saurabh",
    "last name " : "kumar",
    "mobile_no" : 766581990
}
db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)