users = {
    "admin" : {
        "password" : "admin123",
        "failed_logins" : 0
    },
    "devdutt" : {
        "password" : "python123",
        "failed_logins" : 0
    }
}

while True :
    username = input("Enter the username: ")
    username = username.strip().lower()

    if username == "exit" :
        print("Program stopped")
        break
    elif username not in users :
        print("User not found")
    else :
        password = input("Enter the password: ")

        if users[username]["password"] == password :
            print(username, "-LOGIN SUCCESS")
            users[username]["failed_logins"] = 0
        else :
            users[username]["failed_logins"] +=1
            print(username, "- LOGIN FAILED")
            print("Failed logins:",users[username]["failed_logins"])

        if users[username]["failed_logins"] >=3 :
            print(username, "- SECURITY ALERT")
