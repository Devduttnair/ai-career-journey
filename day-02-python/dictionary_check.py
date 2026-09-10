users = {
    "admin" : "active",
    "devdutt" : "actice",
    "guest" : "blocked"
}
username = input("Enter username: ")

username = username.strip().lower()

if username in users :
    print("User exists")
    print("Status:", users[username])
else :
    print("User not found")