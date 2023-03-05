blockchain = []
"""A list holding all the blockchain transaction"""


def get_last_blockchain_value():
    """Get the last element in the blockchain list

    Returns:
        list: The last block in the blockchain
    """
    if len(blockchain) == 0:
        return None
    return blockchain[-1]


def get_transaction_amount_from_user():
    """Gets the transaction amount from the user

    Returns:
        float: Transaction Amount
    """
    return float(input('Enter your transaction amount here:'))


def get_user_choice():
    """Take the user choice

    Returns:
        str: User Choice
    """
    return input("Your choice: ")


def print_blockchain_elements():
    """Prints the whole blockchain
    """
    for block in blockchain:
        print('Output block: ')
        print(block)
    else:
        print('-' * 20)


def add_transaction_value(transaction_amount: float, last_transaction: list = [1]):
    """add transaction value to a new block with a copy from the last transaction

    Args:
        transaction_amount (float): the new transaction amount.
        last_transaction (list, optional): The last transaction amount. Defaults to [1].
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def verify_chain():
    """Verifies that the blockchain have not been manipulated"""
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


# User Interface
waiting_for_input = True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        transaction_amount = get_transaction_amount_from_user()
        add_transaction_value(transaction_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input is invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Manipulated blockchain!!!')
        waiting_for_input = False
else:
    print('User left!')


print('Done!')
