from MongoDBConnector import get_database
dbname = get_database()
collection_name = dbname["notification_data"]
collection_name_latest = dbname["latest_notification_data"]

def add_notification(email, pincode, severity, date, time, title,  text):
    new_notification = {
        "email": email,
        "pincode": pincode,
        "date": date,
        "time": time,
        "severity":severity,
        "text": text,
        "title": title
    }
    collection_name.insert_one(new_notification)
    return {"status": "success", "message": "Notification added successfully"}

def fetch_latest_notification(pincode):
    return collection_name_latest.find_one({"pincode":pincode})

def add_latest_notification(email, pincode, severity, date, time, title, text):
    collection_name_latest.delete_one({"pincode":pincode})
    new_notification = {
        "email": email,
        "pincode": pincode,
        "date": date,
        "time": time,
        "severity":severity,
        "text": text,
        "title": title
    }
    collection_name_latest.insert_one(new_notification)

def fetch_notification_by_admin(email):
    return list(collection_name.find({"email": email}))

def fetch_notification_by_pincode(pincode):
    return list(collection_name.find({"pincode": pincode}))