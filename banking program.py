balance = 0

def Balance():
     print(f"Your current balance is ${balance:.2f}")
    

def deposite():
    global balance
    try:
        money = float(input("How much money do you want to deposit?: "))
        if money < 0:
            print("Please enter a positive amount!")
            return
        balance += money
        print(f"Now, your current balance is ${balance:.2f}")
    except ValueError:
        print("Please enter a valid number!")

def withdraw():
    global balance
    try:
        nikala = float(input("How much money would you like to withdraw?: "))
        if nikala < 0:
            print("Please enter a positive amount!")
            return
        if nikala > balance:
            print("Insufficient funds!")
            return
        balance -= nikala
        print(f"Now, your current balance is ${balance:.2f}")
    except ValueError:
        print("Please enter a valid number!")

banking = True
while banking:
    print("==============Banking System==============")
    print("1.Check Balance\n2.Deposite Money\n3.Withdraw Money\n4.Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        Balance()
    elif choice == "2":
        deposite()       
    elif choice == "3":
        withdraw()
    elif choice == "4":
        quit()
    else:
        print("Please enter a valid input!")
    