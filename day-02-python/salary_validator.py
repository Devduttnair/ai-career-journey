try : 
    salary = int(input("Enter your monthly salary: "))

except ValueError :
    print("Invalid salary. Enter numbers only.")
else :
    if salary >= 100000 :
        print("High income")
    elif salary >= 50000 :
        print("Growing")
    else :
        print("Starting Stage")

        