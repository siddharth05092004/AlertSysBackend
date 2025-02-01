from MongoDBConnector import get_database
dbname = get_database()
collection_name = dbname["user_data"]

def register_user(email, password, name):
    if collection_name.find_one({"email": email}):
        return {"status": "error", "message": "User already exists"}

    new_user = {
        "email": email,
        "password": password,
        "name": name,
    }
    collection_name.insert_one(new_user)
    return {"status": "success", "message": "User registered successfully"}

def update_user_info(email,name,password,phone_number):
    query = {"email": email}
    new_values = {"$set": {"name": name, "password": password, "phone_number": phone_number}}
    result = collection_name.update_one(query, new_values)
    if result.matched_count > 0:
        user = collection_name.find_one({"email": email, "password": password})
        return {"status": "success", "message": "User information updated successfully", "user":user}
    else:
        return {"status": "error", "message": "User not found"}

def update_user_pincode(email,flatno,city,state,country,pincode):
    query = {"email": email}
    new_values = {"$set": {
        "flatno": flatno,
        "city": city,
        "state": state,
        "country": country,
        "pincode": pincode
    }}
    result = collection_name.update_one(query, new_values)
    if result.matched_count > 0:
        user = collection_name.find_one({"email": email})
        return {"status": "success", "message": "User pincode updated successfully", "user":user}
    else:
        return {"status": "error", "message": "User not found"}
