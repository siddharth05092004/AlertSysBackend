from MongoDBConnector import get_database
dbname = get_database()
collection_name_user = dbname["user_data"]
collection_name_admin = dbname["admin_data"]


def get_user_details(email, password):
    user = collection_name_user.find_one({"email": email, "password": password})
    if user:
        return {"status": "success", "type" : "user", "user": user}
    else:
        admin = collection_name_user.find_one({"email": email,"type":"admin", "password": password})
        if admin:
            return {"status": "success", "type" : "admin", "user": admin}
        else:
            return {"status": "error", "message": "Invalid email or password"}