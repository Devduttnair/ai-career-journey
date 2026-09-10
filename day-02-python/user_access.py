users = {
    "admin" : "active",
    "devdutt" : "active",
    "guest" : "blocked"
}

while True :
    username = input("Enter the username: ")
    username = username.strip().lower()

    if username == "exit" :
        print("Program stopped")
        break
    elif username not in users :
        print("User not found")
    elif users[username] == "blocked" :
        print(username, "- access denied")
    else :
        print(username, "- access granted")

    