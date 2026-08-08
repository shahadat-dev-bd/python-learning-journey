correct_pin = "636363"
pin = ""
balance = 10000
choice = ""
withdraw_amount = ""
deposit_amount = ""


while pin != correct_pin:
    pin = input ("Please Enter Pin: ")

while choice != "4":
    print()
    print("========== ATM MENU ==========")
    print()
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    print()

    choice = input("Choose: ")

    if choice == "1":
        print("Your Balance: "  + str(balance)  + "/-")

    elif choice == "2":
        withdraw_amount = int(input("Enter Withdraw Amount: "))

        if withdraw_amount >= 500 and withdraw_amount <= balance:
            balance = balance - withdraw_amount
            print("Please Collect Your Money")
            print("Your Balance: ", balance)
        elif withdraw_amount < 500:
            print("Amount 500-এর কম")
        else:
            print("Insufficient Balance")     

    elif choice  == "3":
          deposit_amount = int(input("Please Deposit Enter Amount: "))
          balance = balance + deposit_amount
          print("Deposit Successfull")
          print("Your Balance is: ", balance)

    elif choice == "4":
        print("Thank you stay with us")

    else:
        print("Invalid input. Please input valid number")    
