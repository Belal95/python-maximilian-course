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
    else:
        print('-' * 20)


def add_transition_value(transaction_amount, last_transaction=[1]):
    """Add a new transaction to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        print(block[0])
        print(blockchain[block_index-1])
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


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
        add_transition_value(transaction_amount, get_last_blockchain_value())
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
        print('Manipulated blockchain!!!')
        waiting_for_input = False
else:
    print('User left!')


print('Done!')
