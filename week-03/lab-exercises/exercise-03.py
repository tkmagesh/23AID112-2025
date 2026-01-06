
### Exercise 3: Banking Transaction Processor

""" 
Build a banking app to process transactions. Accounts are in a dictionary {account_id (int): balance (float)}. Transactions are a list of tuples (account_id, amount, type='deposit' or 'withdraw'). Loop through transactions, use conditionals for deposit/withdraw, handle errors for insufficient funds or invalid type, store processed accounts in a set, and return a tuple of (final_balances_dict, processed_accounts_set). 
"""

def process_transactions(accounts, transactions):
    # Loop through transactions
    # Error handling for insufficient funds or invalid type
    # Conditional for deposit/withdraw
    # Use set for processed accounts
    # Return tuple of (final_balances_dict, processed_accounts_set)
    pass

# Example usage
accounts = {101: 500.0, 102: 300.0}
transactions = [(101, 100.0, 'deposit'), (102, 400.0, 'withdraw'), (101, 50.0, 'invalid')]  # Invalid will trigger error
print(process_transactions(accounts, transactions))  # Example call

