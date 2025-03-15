# Soutree Slot Machine 

from random import choice
from sys import stdout
from time import sleep

def spin_row():
    symbols = [ '🍒', '🍋', '🍇', '⭐']
    result = [choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("\n++++++++++++++++++++++")
    print("|  ", end="")
    print("  |  ".join(row), end="")
    print("  |")
    print("++++++++++++++++++++++")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 10
        elif row[0] == '🍋':
            return bet * 15
        elif row[0] == '🍇':
            return bet * 20
        else:
            return bet * 100
    else:
        return 0
        

def main():
    balance = 100

    ascii_art = '''
=====================================
   Welcome to Soutree Slot Machine!
=====================================
  Symbols:  🍒    🍋    🍇     ⭐
  Redwards: 10x   15x   20x   100x
=====================================
'''
    print(ascii_art)


    while balance > 0:
        print("\nYou can press 'q' to quit")
        print(f"Current Balance: ${balance}")
        bet = input("Place your bet amount: ")

        if bet.lower() == 'q':
            print("\nExiting Game.")
            break

        if not bet.isdigit():
            print("\nPlease enter a valid number.")
            continue

        bet = int(bet)
        
        if bet > balance: 
            print("\nInsufficient balance")
            continue
        
        if bet <= 0:
            print("\nBet must be greater than 0.")
            continue
        
        # Creating row at random            
        row = spin_row()

        # ASCII animation
        print() 
        ascii = "Spinning....."
        for i in range(7, 13):
            stdout.write(f"\r{ascii[:i+1]}")
            sleep(0.08)        

        # Printing the randomly generated row
        print_row(row)

        # Checking the Payout: 
        payout = get_payout(row, bet)

        if payout == 0:
            print("You lost this round!")
        else: 
            print(f"You won ${payout}!")
            balance += payout

        balance -= bet
    else:
        print("\nGAME OVER!\nAmount 0. You can't play anymore.")
    
    print(f"\nYour final balance is: ${balance}\n")

if __name__ == "__main__":
    main()