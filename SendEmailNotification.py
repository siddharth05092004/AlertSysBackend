from courier.client import Courier
import os
from dotenv import load_dotenv
from MongoDBConnector import get_database
dbname = get_database()
collection_name = dbname["user_data"]

load_dotenv()

client = Courier(
  authorization_token=os.getenv("COURIER_API")
)

def send_email_notification_helper(email, name, title,text):
  resp = client.send(
    message={
      "to": {
        "email": email
      },
      "content": {
        "title": title,
        "body": text
      },
      "data": {
        "name": name
      }
    }
  )

  return(resp)

def send_email_notification(pincode,title,text):
  users = collection_name.find({"pincode": pincode})
  for user in users:
    email = user.get("email")
    name = user.get("name")
    send_email_notification_helper(email, name, title, text)
