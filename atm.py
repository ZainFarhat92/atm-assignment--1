balance = 1000  # Starting balance
password = "0000" # Password used for login
transactionCounter = 0  # Track the number of transactions deposits and withdrawl
failedWithdrawals = 0  # Track the number of failed withdrawals
maxfailedAttempts = 3  # Maximum allowed failed attempts

# Login to the ATM
print("Welcome to the ATM!")
loginPassword = input("Please enter your password: ")

if loginPassword != password:
    print("Incorrect password")
else:
    # Start the menu loop
    while True:
        print("Welcome to The ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Please enter your choice (1-4): ")
        
        if choice == '1': #Check Balance
            print("Your current balance is: $" + str(balance))

        elif choice == '2': # Deposit Money
            try:
                deposit = float(input("Enter the amount to deposit: "))
                if deposit > 0:
                    balance = balance + deposit
                    print("$" + str(deposit) + " deposited successfully.")
                    print( "Your New balance after deposit is: $" + str(balance))
                    transactionCounter = transactionCounter + 1  # Increment transaction count
                    
                else:
                    print("Deposit amount must be positive")
            except ValueError:
                print("Invalid input")
        
        elif choice == '3': # Withdraw Money
            try:
                withdraw = float(input("Enter the amount to withdraw: "))
                if withdraw > 0:
                    if withdraw <= balance:
                        balance = balance - withdraw
                        print("$" + str(withdraw) + " withdrawn successfully." )
                        print( "Your New balance after withdrawl is: $" + str(balance))
                        transactionCounter = transactionCounter + 1  # Increment transaction count
                    else:
                        print(" Not Enough balance.")
                        failedWithdrawals = failedWithdrawals + 1  # Increment failed withdrawal count
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid input.")
            
            # a warning if more than 3 failed withdrawals were attempted.
            if failedWithdrawals > maxfailedAttempts :
                print("Warning Please recheck your balance too many failed withdrawls attempts")
        elif choice == '4': #Exit
            print("Thank you for using the ATM.")
            if transactionCounter > 0:
                print("Total successful transactions: " + str(transactionCounter))
            if failedWithdrawals > 0:
                print("Failed withdrawals: " + str(failedWithdrawals))
        else:
            # Invalid Option
            print(" Please select a valid option from (1-4).")