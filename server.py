from flask import Flask, jsonify, request
import os
from bson import json_util
import json

from UserDetailFetch import get_user_details
from NewUserRegistration import register_user, update_user_info, update_user_pincode
from NotificationUtility import fetch_notification_by_admin, fetch_notification_by_pincode, add_notification, add_latest_notification, fetch_latest_notification
from SendEmailNotification import send_email_notification
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://disaster-management-gray.vercel.app"}},supports_credentials=True)
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "https://disaster-management-gray.vercel.app"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response


# working 
@app.route('/api/userlogin', methods=['POST'])
def user_login():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    if hash == os.getenv('HASH'):
        email = data.get('email')
        password = data.get('password')
        result = get_user_details(email, password)
        return json.loads(json_util.dumps(result))
    else:
        return jsonify({'message': 'Invalid Hash'})
    
# working     
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    if hash == os.getenv('HASH'):
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        result = register_user(email, password, name)
        return json.loads(json_util.dumps(result))
    

# working
@app.route('/api/user/pincode', methods=['POST'])
def update_user_pincode_api():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    if hash == os.getenv('HASH'):
        email = data.get('email')
        flatno = data.get('flatno')
        city = data.get('city')
        state = data.get('state')
        country = data.get('country')
        pincode = data.get('pincode')
        result = update_user_pincode(email, flatno, city, state, country, pincode)
        return json.loads(json_util.dumps(result))
    

# working
@app.route('/api/user/info', methods=['POST'])
def update_user_info_api():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    if hash == os.getenv('HASH'):
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        mobile_number = data.get('mobile_number')
        result = update_user_info(email, name, password, mobile_number)
        return json.loads(json_util.dumps(result))


@app.route('/api/notification/admin', methods=['POST'])
def get_notifications_by_admin():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    email = data.get('email')
    if hash == os.getenv('HASH'):
        result = fetch_notification_by_admin(email)
        return json.loads(json_util.dumps(result))

@app.route('/api/notification/pincode', methods=['POST'])
def get_notifications_by_pincode():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    pincode = data.get('pincode')
    if hash == os.getenv('HASH'):
        result = fetch_notification_by_pincode(pincode)
        return json.loads(json_util.dumps(result))


@app.route('/api/notification', methods=['POST'])
def add_notification_api():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    hash = data.get('hash')
    if hash == os.getenv('HASH'):
        email = data.get('email')
        pincode = data.get('pincode')
        severity = data.get('severity')
        date = data.get('date')
        time = data.get('time')
        text = data.get('text')
        title = data.get('title')
        add_latest_notification(email, pincode, severity, date, time, title, text)
        result = add_notification(email, pincode, severity, date, time, title, text)
        # send_email_notification(pincode, title, text)
        return json.loads(json_util.dumps(result))



@app.route('/api/notification/latest', methods=['POST'])
def add_latest_notification_api():
    data = request.json
    try:
        hash = data.get('hash')
    except:
        return jsonify({'message': 'Invalid Hash'})
    if hash == os.getenv('HASH'):
        pincode = data.get('pincode')
        result = fetch_latest_notification(pincode)
        return json.loads(json_util.dumps(result))
    
if __name__ == '__main__':
    import os
    port = int(os.getenv("PORT", 5000))  # Use Render's provided port or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
