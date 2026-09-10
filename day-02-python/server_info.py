server = {
    "name" : "AI-Server",
    "ip" : "192.168.1.10",
    "status" : "running",
    "cpu_usage" : 35
}

print(server["name"])
print(server["ip"])

server["cpu_usage"] = 75
server["secure"] = True

print(server)

if server["cpu_usage"] >= 80 :
    print("Warning: High CPU Usage")
else :
    print("CPU Usage normal")