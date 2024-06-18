import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Minimum deposit amount is $1")
        else:
            print("Invalid amount. Please enter a valid amount in numbers only.")
            
    return amount
    
def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines. Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
        return lines
     
def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount myst be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to make this bet. Your current balance is ${balance}.")
        else:
            break
    
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

main()
