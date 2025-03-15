# Python Banking Program 

def show_balance(balance):
    print(f"\nAccount Balance: {balance:.2f}\n")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0: 
        print("That's not a valid amount!\n")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    if balance < amount: 
        print(f"Insufficient balance! You cannot withdraw {amount}\n")
        return 0
    elif balance < 0:
        print("Amount should be greater than 0")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program Main Menu")
        print("==========================")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        choice = int(input("Enter choice (1 - 4): "))
        match choice: 
            case 1: 
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3: 
                balance -= withdraw(balance)
            case 4: 
                is_running = False
            case _:
                print("Invalid Input!")
    print("Thank you, have a nice day!")

if __name__ == "__main__":
    main()