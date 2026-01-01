import random
import gamedata

def get_random_account():
    """Returns a random account from the gamedata."""
    return random.choice(gamedata.data)

def format_account(account):
    """Formats the account data into a printable string."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def account_refresh(account):
    """Refreshes the account data by returning a new random account."""
    new_account = get_random_account()
    while new_account == account:
        new_account = get_random_account()
    return new_account

account_A = get_random_account()
account_B = get_random_account()
score = 0

print("Welcome to the Higher Lower Game!")
print("Compare the follower counts of different Instagram accounts.")
print(f'\n\n Compare A: {format_account(account_A)}. \n\n vs \n\n Compare B: {format_account(account_B)}.\n\n')

choice = input("\nWho has more followers? Type 'A' or 'B': \n").upper()

while score >= 0:
    if choice == 'A':
        if account_A['follower_count'] > account_B['follower_count']:
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            account_B = account_refresh(account_B)
            account_A = account_refresh(account_A)
            print(f'\n\n Compare A: {format_account(account_A)}. \n\n vs \n\n Compare B: {format_account(account_B)}.\n\n')
            choice = input("\nWho has more followers? Type 'A' or 'B': \n").upper()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
    elif choice == 'B':
        if account_B['follower_count'] > account_A['follower_count']:
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            account_A = account_refresh(account_A)
            account_B = account_refresh(account_B)
            print(f'\n\n Compare A: {format_account(account_A)}. \n\n vs \n\n Compare B: {format_account(account_B)}.\n\n')
            choice = input("\nWho has more followers? Type 'A' or 'B': \n").upper()
        else:
            print(f"\nSorry, that's wrong. Final score: {score}.\n")
            break
    else:
        print("\nInvalid input. Please type 'A' or 'B'.\n")
        choice = input("\nWho has more followers? Type 'A' or 'B': \n").upper()