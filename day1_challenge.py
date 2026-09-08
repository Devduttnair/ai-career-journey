name = input("Enter your name:")
salary = int(input("Enter your monthly salary:"))
expenses = int(input("Enter your monthly expenses:"))

print("Hello",name)


def calculate_savings(salary,expenses):
    savings = salary - expenses
    return savings

def check_financial_status(savings):
    print("Monthly savings: ", savings)
    if savings >= 50000 :
        print("Financial Status : Excellent")
    elif savings >= 20000:
        print("Financial Status : Good")
    elif savings >= 1:
        print("Financial Status : Low")
    else :
        print("Financial Status : Warning")

savings = calculate_savings(salary,expenses)
check_financial_status(savings)