try :
    age = int(input("Enter your age: "))
    print("Your age is: ",age)

except : 
    print("Invalid input. Please enter a number.")
else :
    print("Valid age:", age)