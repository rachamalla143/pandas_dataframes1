import logging
import pymongo

logging.basicConfig(filename='or_con_mongodb.log', level=logging.DEBUG, format = '%(name)s : %(levelname)s : %(asctime)s : %(message)s')
client = pymongo.MongoClient("mongodb+srv://rachamalla:Gowri143.@rachamalla.eurulow.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d =[ {
    "company_details":["cyent","NTT Data","legato","amdocs"],
    "name_worker":"rachamalla nagaraju",
    "emp_id":"NR5251",
    "mail_id":"rachamalla.mf@gmail.com",
    "contact":9701583577

},

        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

database = client["inventory"]
collection = database["or_mongo_pro"]
## storing the data in table on mongodb server.
collection.insert_many(d)


# we are filtering as "status":"A" related records only....!
#d1 = collection.find({"status":"A"})

# where status is A or P related records we are printing.....!
#d1 = collection.find({"status": {'$in': ['A', 'P']}})


# we are printing as C > related status records we are gathering....!
#d1 = collection.find({"status": {'$gt': 'C'}})


#we are printing as QTY>= 100 related records in mongoDB
#d1 = collection.find({"qty": {"$gte": 100}})


# we are printing as multiple column based filter
#d1 = collection.find({"status": {"$in":["A" , "P"]}})

d1 = collection.find({"$and": [{"status": {"$in": ["A", "P"]}}]})
for i in d1:
    logging.info(i)

