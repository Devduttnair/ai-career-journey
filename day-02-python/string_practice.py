while True:
    command = input("Enter command: ")
    command = command.strip().lower()

    if command == "status" :
        print("System is running")
    elif command == "help" :
        print("Available commands: status, help, exit")
    elif command == "exit" :
        print("Program stopped")
        break
    else:
        print("Unknown Commamd")