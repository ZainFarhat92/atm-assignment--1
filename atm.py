balance = 1000  # Starting balance
password = "0000" # Password used for login
transactionCounter = 0  # Track the number of transactions deposits and withdrawl

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
        
