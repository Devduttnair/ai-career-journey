number = 1

while number <= 5 :
    print("Number:", number)
    number = number + 1

print("Loop finished")

while True:
    answer = input("Type 'exit' to stop: ")

    if answer == "exit":
        print("Stopping program")
        break
    else:
        print("You entered:",answer)

        