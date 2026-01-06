
### Exercise 3: Banking Transaction Processor

""" 
Build a banking app to process transactions. Accounts are in a dictionary {account_id (int): balance (float)}. Transactions are a list of tuples (account_id, amount, type='deposit' or 'withdraw'). Loop through transactions, use conditionals for deposit/withdraw, handle errors for insufficient funds or invalid type, store processed accounts in a set, and return a tuple of (final_balances_dict, processed_accounts_set). 
"""



def process_transactions(accounts, transactions):
    """
    Processes banking transactions for deposits and withdrawals.
    
    :param accounts: dict - {account_id: balance}
    :param transactions: list of tuples - (account_id, amount, type)
    :return: tuple - (final_balances_dict, processed_accounts_set)
    """
    # Copy accounts to avoid modifying original
    final_balances = accounts.copy()  # Dict for final balances
    processed_accounts = set()  # Set for unique processed account_ids
    
    # Loop through each transaction
    for trans in transactions:
        account_id, amount, trans_type = trans  # Unpack tuple
        
        # Error handling: Check if account exists
        try:
            if account_id not in final_balances:
                raise KeyError(f"Account {account_id} not found.")
            
            # Conditional branching: Handle deposit or withdraw
            if trans_type == 'deposit':
                final_balances[account_id] += amount
            elif trans_type == 'withdraw':
                if final_balances[account_id] < amount:
                    raise ValueError(f"Insufficient funds in account {account_id}.")
                final_balances[account_id] -= amount
            else:
                raise ValueError(f"Invalid transaction type '{trans_type}'.")
            
            processed_accounts.add(account_id)  # Add to set
        except (KeyError, ValueError) as e:
            # Handle error by skipping and logging
            print(e)  # For demonstration
            continue
    
    # Return results as tuple
    return final_balances, processed_accounts

# Example usage
accounts = {101: 500.0, 102: 300.0}
transactions = [(101, 100.0, 'deposit'), (102, 400.0, 'withdraw'), (101, 50.0, 'invalid')]  # Invalid will trigger error
print(process_transactions(accounts, transactions))  # Example call

