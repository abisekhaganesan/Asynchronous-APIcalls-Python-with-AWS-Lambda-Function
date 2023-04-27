import json

# Function responsible for authenticating the user with a username and password
def user_auth(username,password):
    # Values are taken as static and stored locally
    authorized_users = {
        "alice": "password123",
        "bob": "secret456",
        "charlie": "letmein789"
    }
    
    # Check if the provided username is in the authorized_users dictionary and if the associated password matches the provided password
    if username in authorized_users and authorized_users[username] == password:
        response_body = {"message": "Login successfull"}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    else:
        response_body = {"message": "Login unsuccessfull"}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response

# Function returns the number of active users for a specific month or all months.
def login_log(month):
    monthly_active_user = {
        "January":"23",
        "February":"20",
        "March":"18",
        "April":"25"
    }
    
    # If the month is not specified, returns an error message
    if not month:
        response_body = {"message": "Month is not mentioned"}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    elif month in monthly_active_user:
        response_body = {"message": f"{month} month active users are {monthly_active_user[month]}."}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    elif month == "All":
        len_month = len(monthly_active_user)
        response_body = {"no_of_month": len_month,"monthly_active_user":monthly_active_user}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    # If the month is not in the database, returns an error message
    else:
        response_body = {"message": "The record is not in the database."}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
# Function returns user metadata for a specific user or all users
def meta_data(user):
    user_meta_data = {
        "101":{
            "Name":"Abi",
            "Gender":"F",
            "Age":"25",
            "Address":"No 2 Anna Nagar",
            "Phone":"789456123",
            "Roll":"Manager"
        },
        "102":{
            "Name":"Divya",
            "Gender":"F",
            "Age":"24",
            "Address":"No 6 KK Nagar",
            "Phone":"15486325",
            "Roll":"Sales"
        },
        "103":{
            "Name":"Raj",
            "Gender":"M",
            "Age":"27",
            "Address":"No 9 Green Nagar",
            "Phone":"852147963",
            "Roll":"Cashier "
        },
        "104":{
            "Name":"Jay",
            "Gender":"M",
            "Age":"30",
            "Address":"No 9 Anna Nagar",
            "Phone":"789456123",
            "Roll":"Receptionist"
        },
        "105":{
            "Name":"Zara",
            "Gender":"F",
            "Age":"28",
            "Address":"No 11 KK Nagar",
            "Phone":"456789123",
            "Roll":"Cashier"
        }
    }
    # If the user is not specified, returns an error message
    if not user:
        response_body = {"message": "User is not mentioned"}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    elif user in user_meta_data:
        response_body = {"User":user,"Meta_data":user_meta_data[user]}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
        
    elif user == "All":
        len_rec = len(user_meta_data)
        response_body = {"no_of_records": len_rec,"records":user_meta_data}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
    
    # If the user is not in the database, returns an error message
    else:
        response_body = {"message": "The record is not in the database."}
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response

# Main entry point of the lambda function
def lambda_handler(event, context):
    # Sample Req Format 
    #
    # {"data_json": "{\"header\": \"user_auth\", \"username\": \"johndoe\", \"password\": \"secret123\"}"}
    # {"data_json": "{\"header\": \"login_log\", \"month\": \"January\"}"}
    # {"data_json": "{\"header\": \"meta_data\", \"user\": \"101\"}"}
    #
    # Read the JSON request from the event
    request = json.loads(event['body'])
    
    data_json = json.loads(request['data_json'])
    # Calls the appropriate function based on the header
    header = data_json['header']

    if header == "user_auth":
        username = data_json['username']
        password = data_json['password']
        
        # Function Call 
        result = user_auth(username,password)
    
    elif header == "login_log":
        month = data_json['month']
        
        # function Call
        result = login_log(month)
    
    elif header == "meta_data":
        user = data_json['user']
        
        # Function Call
        result = meta_data(user)
    
    else:
        # Build the response body
        response_body = {"message": "Not a proper header"}
        # Build the HTTP response
        result = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return result

    return result
    