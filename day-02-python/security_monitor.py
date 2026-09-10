users = [
    {
        "username" : "admin",
        "authenticated" : True,
        "failed_logins" : 0
    },
    {
        "username" : "Devdutt",
        "authenticated" : True,
        "failed_logins" : 2
    },
    {
        "username" : "unknown_user",
        "authenticated" : False,
        "failed_logins" : 7
    }
]

for user in users :
    if user["authenticated"] == False :
        print(user["username"], "- ACCESS DENIED")
    elif user["failed_logins"] >= 5 :
        print(user["username"], "- SECURITY ALERT")
    else :
        print(user["username"], "- ACCOUNT OK")
