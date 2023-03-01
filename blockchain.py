blockchain = []
"""A list holding all the blockchain transaction"""


def get_last_blockchain_value():
    """Get the last element in the blockchain list"""
    if len(blockchain) == 0:
        return None
    return blockchain[-1]


def get_transaction_amount_from_user():
    """Gets the transaction amount from the user"""
    return float(input('Enter your transaction amount here:'))


def get_user_choice():
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print('Output block: ')
        print(block)


def add_transition_value(transaction_amount, last_transaction=[1]):
    """Add a new transaction to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
    """
    blockchain.append([last_transaction, transaction_amount])


# transaction_amount = get_transaction_amount_from_user()
# add_transition_value(transaction_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        transaction_amount = get_transaction_amount_from_user()
        add_transition_value(transaction_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        break
    else:
        print('Input is invalid, please pick a value from the list!')

print('done!')
