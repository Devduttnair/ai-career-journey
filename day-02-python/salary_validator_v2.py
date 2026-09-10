while True:
    try:
        salary = int(input("Enter your monthly salary: "))

        if salary >= 100000:
            print("High income")
        elif salary >= 50000:
            print("Growing")
        else:
            print("Starting stage")
        break

    except ValueError:
        print("Invalid salary. Enter numbers only.")
