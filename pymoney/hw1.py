#! python3

if __name__ == '__main__':

    # Get current money in integer form
    current_money = int(input('How much money do you have? '))

    # Get incoming record (an expense or income)
    update_record = input('Add an expense or income record with description and amount:\n')
    
    # Ensure that record is of two parts (length = 2)
    record = update_record.split()
    assert(len(record) == 2), 'Record should be of length 2'

    # Split string into two strings (name and value)
    rec_name, rec_value = record

    # Calculate current balance and output to screen
    current_money += int(rec_value)
    print(f'Now you have {current_money} dollars.')
