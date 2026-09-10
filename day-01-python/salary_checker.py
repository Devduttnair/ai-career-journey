name = input("Enter your name: ")
salary = int(input("Enter your monthly salary: "))
expenses = int(input("Enter your monthly expenses: "))
savings = salary - expenses

print("Hello", name)

if salary >= 100000 :
    print("High income")
elif salary >= 50000 :
    print("Growing")
else :
    print("Starting stage")

print("Monthly Savings: ", savings)

if savings >= 50000 :
    print("Excellent Savings")
elif savings >= 20000 :
    print("Good savings")
elif savings >= 1:
    print("Low Savings")
else :
    print("Warning: No savings")
    