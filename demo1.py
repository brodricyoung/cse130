 
def create_account(accounts, account_number: str, initial_balance: float): 
    accounts[account_number] = initial_balance

def deposit(accounts, account_number: str, amount: float):
    try:
        assert accounts[account_number]
        accounts[account_number] += amount
    except: 
        print(f"The account {account_number} does not exist.")
    

def withdraw(accounts, account_number: str, amount: float):
    try:
        assert accounts[account_number]
        accounts[account_number] -= amount
    except: 
        print(f"The account {account_number} does not exist.")
    

def get_balance(accounts, account_number: str) -> float:
    try:
        assert accounts[account_number]
        return accounts[account_number]
    except: 
        print(f"The account {account_number} does not exist.")
    

def main():
    accounts = {}
    create_account(accounts, '12345', 0)
    deposit(accounts, '12345', 500)
    withdraw(accounts, '12345', 25)
    balance = get_balance(accounts, '12345')
    print(f'Your account has a balance of ${balance:.2f}')

if __name__ == "__main__":
    main()
 
 