user = {
    "username" : "devdutt",
    "failed_logins" : 0
}

print("Before:", user["failed_logins"])

user["failed_logins"] = user["failed_logins"] + 1

print("After first failure:", user["failed_logins"])

user["failed_logins"] +=1

print("After second failure:", user["failed_logins"])