#! python3

import os
import sys
import stat
import time

def initialize():
    
    initial_money = 0
    records       = []

    completion_flag = False

    while not completion_flag:

        try:
            with open('records.txt', 'r') as ifstream:
    
                try:
                    # Read in the initial amount of money
                    initial_money = int(ifstream.readline())

                except ValueError:
                    sys.stderr.write('[ValueError] Initial amount of money cannot be converted into integer with base 10.\n')
                    sys.stderr.write('[Quick fix]  Initial amount of money overwritten as $0\n\n')
    
                    initial_money = 0

                # Read all remaining lines in records.txt
                records_list = ifstream.readlines()

                # Consequently, convert the remaining records in the file into list of pairs (record name, amount)
                for line in records_list:

                    pair = line.split()
                    
                    # An unacceptable format of record, skip
                    if(len(pair) != 2):
                        sys.stderr.write(f'[Unrecognized Record] The record \'{line[:-1]}\' is in an incorrect format.\n')
                        sys.stderr.write(f'[Quick fix]           The record has been ignored.\n\n')
                        continue

                    try:
                        record_name = pair[0]
                        record_amt  = int(pair[1])

                    except ValueError:
                        sys.stderr.write(f'[ValueError] The amount of money in record \'{line[:-1]}\' cannot be converted into integer with base 10.\n')
                        sys.stderr.write(f'[Quick fix]  The amount of money in the record is parsed as $0\n\n')

                        record_amt = 0
                
                    # Place the record into 
                    records.append((record_name, record_amt))

            # Ends without error: file parsing complete
            completion_flag = True


        # No old records can be found. Prompt user for initial amount of money
        except FileNotFoundError:
        
            print('\tNo old records can be found. Please make new record with the following step.\n\n')

            # Repeat until users input an integer
            while True:
                try:
                    initial_money = int(input('\tPlease input the initial starting amount of money: '))
                except ValueError:
                    print('[ValueError] Your input cannot be converted into integer with base 10.')
                else:
                    break
        
            print('\tNew record created! Thank you very much.\n\n\n')
            
            # Ends wtihout error: file parsing complete
            completion_flag = True

        # Does not have access to records.txt.
        except PermissionError:
            
            sys.stderr.write('[PermissionError] records.txt cannot be opened.\n')
            sys.stderr.write('[Quick fix]       Attempting to unlock permission...\n\n')

            # Unlock restriction
            os.chmod('records.txt', stat.S_IREAD | stat.S_IWRITE)

            # Repeat the while loop
            continue

        time.sleep(3)


    return initial_money, records



def add(records):

    print('\tAdd some expense or income records with description and amount with the format:')
    print('\tdesc_1 amount_1, desc_2 amount_2, desc_3 amount_3, ...\n')


    # First, split input by ',', then ' ' (might need to remove residual ' ')
    input_records = input('\tRecords: ').split(',')
    new_records_list = []
    for record in input_records:
        temp_list = record.split(' ')
        
        # Remove the residual '' at front of the records (if exists)
        if(temp_list and (temp_list[0] == '')):
            temp_list.pop(0)

        new_records_list.append(temp_list)


    # Second, parse every (name, amount) pair and append to records (a list of (record, name) tuple)
    for pair in new_records_list:

        if(len(pair) != 2):
            sys.stderr.write(f'[Unrecognized record] The record \'{pair}\' is in an unrecognized format.\n')
            sys.stderr.write('[Quick fix]           The record has been ignored.\n\n')
            continue

        valid_flag = False
        while not valid_flag:
            try:
                pair[1] = int(pair[1])
                
                valid_flag = True

            except ValueError:
                sys.stderr.write(f'[Unrecognized record] The amount value of record \'{pair}\' cannot be converted to an integer of base 10.\n')
                sys.stderr.write('[Quick fix]           Prompt user again.\n\n')

                pair[1] = input(f'\tFor record \'{pair[0]}\',\n\tPlease input its amount: ')
                continue
        
        records.append((pair[0], pair[1]))

    print('\n\tAdding record successful! Returning...\n')
    time.sleep(3)

    return records



def view(initial_money, records, pause = True):
    
    # Print header
    print('\t' + '-' * 70)
    print('\t{:-^70s}'.format('RECORD'))
    print('\t' + '-' * 70 + '\n')

    # Print intial money
    print('\t      {:40s} : ${:20d}\n'.format('Initial Money', initial_money))

    print('\t' + '-' * 70 + '\n')

    # Print records while summing the total
    total = initial_money
    for (i, pair) in enumerate(records):

        print(f'\t{(i+1):03d}   {pair[0]:40s} : ${pair[1]:20d}')
        
        total += pair[1]

    print('\n\t' + '-' * 70 + '\n')

    # Print total
    print('\t      {:40s} : ${:20d}\n\n'.format('Balance', total))
    

    # Wait for user
    if(pause):
        input('\tPress any key to continue')

    return None



def delete(initial_money, records):

    # First, display records to the user
    view(initial_money, records, pause = False)

    # Secondly, prompt the user for the indices of the records they want to delete
    print('\tEnter the indices of the records you wish to delete in the format: index_1 index_2 index_3 ...')
    while True:
        try:
            indices_list = [int(i) for i in input('\tIndices: ').split(' ')]
        except ValueError:
            sys.stderr.write('[ValueError] Please follow the correct format: index_1 index_2 index_3 ...\n')
            sys.stderr.write('[Quick fix]  Prompting user for input.\n\n')
            continue
        else:
            break


    # Filter legal indices
    legal = []
    for index in indices_list:

        if((index < 1) or (index > len(records))):
            sys.stderr.write(f'[IndexError] The index {index} is out of bound.\n')
            sys.stderr.write(f'[Quick fix]  The index has been ignored.\n\n')
            continue

        legal.append(index)

    if(legal == []):
        print('\n\tYou have no records to delete. Returning...\n')
        time.sleep(3)
        return records


    # Sort indices
    legal = sorted([i for i in {i for i in legal}])

    # Third, reconfirm with user that these records are going to be deleted permanently
    print('\n\tThese records are going to be deleted:')
    print('\t' + '-' * 70 + '\n')
    for index in legal:
        print(f'\t{index:03d}   {records[index - 1][0]:40s} : ${records[index - 1][1]:20d}')
    print('\t' + '-' * 70 + '\n')
    
    # If the user is sure, delete all the specified records
    if(input('\tPress Y if you are sure. Otherwise, press any other key to cancel deletion ').lower() == 'y'):
        

        new_records = []
        for (i, pair) in enumerate(records):

            if((legal == []) or (i != legal[0] - 1)):
                
                new_records.append(pair)
                continue

            legal.pop(0)

        records = new_records
        print('\n\tDeletion successful.\n\n')

    else:
        print('\n\tDelete aborted.\n\n')

    time.sleep(3)
    return records



def save(initial_money, records):

    completion_flag = False

    while not completion_flag:

        try:

                # Open the file with overwrite option
                # Reason 1: We may had encountered records with incorrect mode. This is a chance to remove them.
                # Reason 2: Simplicity, might need to avoid repetition with append mode.  
                with open('records.txt', 'w') as ofstream:
            
                    # First, write the initial_money
                    ofstream.write(str(initial_money) + '\n')

                    # Second, write the records into a buffer (list of strings)
                    buffer = []
                    for pair in records:
                
                        if len(pair) != 2:
                            sys.stderr('[Unrecognized Record] The record \'{pair}\' is in an incorrect format\n')
                            sys.stderr('[Quick fix]           The record has been ignored.\n\n')
                            continue
    
                        try:
                            buffer.append(pair[0] + ' ' + str(pair[1]) + '\n')
                        except TypeError:
                            sys.stderr('[Unrecognized Record] The record \'{pair}\' is in an incorrect format\n')
                            sys.stderr('[Quick fix]           The record has been ignored.\n\n')
                            continue
    
                    # Third, write buffer into records.txt
                    ofstream.writelines(buffer)

                # Ends without error: complete
                completion_flag = True

        # Do not have permission to records.txt
        except PermissionError:
        
            sys.stderr.write('[PermissionError] records.txt cannot be opened.\n')
            sys.stderr.write('[Quick fix]       Attempting to unlock permission...\n\n')

            # Unlock restriction
            os.chmod('records.txt', stat.S_IREAD | stat.S_IWRITE)

            # Repeat while loop
            continue

    print('\n\tRecords successfully saved into records.txt.\n\n')

    time.sleep(3)


if __name__ == '__main__':
    
    os.system('clear')
    print('\tWelcome back to PyMoney.\n\n')

    initial_money, records = initialize()

    # Constant string literal`
    display_text = '''
        Instructions menu:

        [*] add    : Add record(s)
        [*] view   : View existing record(s)
        [*] delete : Delete a record
        [*] exit   : Save existing record(s) and quit program

    
        What do you want to do? 
        '''

    if(records):
        print('\tHere is a summary of previous record.\n')
        view(initial_money, records)


    while True:
        
        os.system('clear')
        command = input(display_text).lower()


        if command == 'add':
            os.system('clear')
            print('\tYou have selected ADD\n\n')
            records = add(records)
            continue

        if command == 'view':
            os.system('clear')
            print('\tYou have selected VIEW\n\n')
            view(initial_money, records)
            continue

        if command == 'delete':
            os.system('clear')
            print('\tYou have selected DELETE\n\n')
            records = delete(initial_money, records)
            continue

        if command == 'exit':
            print('\tYou have selected EXIT\n\n')
            os.system('clear')
            save(initial_money, records)
            break

        sys.stderr.write(f'\n[Invalid Command] Cannot parse \'{command}\'. Try again\n\n')
        time.sleep(3)


    print('\tThis PyMoney session will soon end. See you!')
