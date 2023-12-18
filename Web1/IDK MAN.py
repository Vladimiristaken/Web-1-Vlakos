while True:
    
    number=input("Hello, please enter any number or the word quit to exit:")
    if number == "quit":
        print("Thank you for using the program")
        break
    else:
        number = int(number)
        for number in range(0, number):
            print(end="*")
        print()
