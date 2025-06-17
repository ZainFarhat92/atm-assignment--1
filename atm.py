balance = 1000  # Starting balance
password = "0000" # Password used for login

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
        
        if choice == '1': # Check Balance
            print("Your current balance is: $" + str(balance))
        
