correct_pin = "636363"
pin = ""
balance = 10000
choice = ""
withdraw_amount = ""
deposit_amount = ""
count = 0


while count < 3:
    pin = input ("Please Enter Pin: ")

    if pin != correct_pin:
        count +=1
    else:
        break

if count == 3:
    print("Access Denied")

else:
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
            try:
                withdraw_amount = int(input("Enter Withdraw Amount: "))

                if withdraw_amount >= 500 and withdraw_amount <= balance:
                    balance = balance - withdraw_amount
                    print("Please Collect Your Money")
                    print("Your Balance: ", balance)
                elif withdraw_amount < 500:
                    print("Amount 500-এর কম")
                else:
                    print("Insufficient Balance")
            except ValueError:
                print("Please Enter a Valid Number")   

        elif choice  == "3":
            try:
                deposit_amount = int(input("Please Enter Deposit Amount: "))

                if deposit_amount >= 500 and deposit_amount % 500 == 0 :
                    balance = balance + deposit_amount
                    print("Deposit Successfull")
                    print("Your Balance is: ", balance)
                else:
                    print("Invalid Deposit Amount")
            except ValueError:
                print("Please Enter a Valid Number")        

        elif choice == "4":
            print("Thank you stay with us")

        else:
            print("Invalid input. Please input valid number")    
