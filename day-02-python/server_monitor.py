servers = [
    {
        "name" : "AI-Server",
        "status" : "running",
        "cpu_usage" : 75
    },
    {
        "name" : "Web-Server",
        "status" : "running",
        "cpu_usage" : 92
    },
    {
        "name" : "Database-Server",
        "status" : "stopped",
        "cpu_usage" : 0
    }
]

for server in servers :
    if server["status"] == "stopped" :
        print(server["name"], "- SERVER STOPPED")
    elif server["cpu_usage"] >= 80 :
        print(server["name"], "- HIGH CPU")
    else :
        print(server["name"], "- HEALTHY")

