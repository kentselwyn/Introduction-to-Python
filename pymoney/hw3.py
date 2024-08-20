#! python3

import os
import sys
import stat
import time
import itertools

class Categories:
    '''
    ====================================================================================================================================
    |                                                                                                                                  |
    | Categories is a class that maintains the category list and corresponding complementary methods.                                  |
    |                                                                                                                                  | 
    ====================================================================================================================================
    | Available usable methods and their purposes:                                                                                     |
    ====================================================================================================================================
    | [1]  view()                    : prints out a comprehensive and indented list of the categories.                                 |
    |                                                                                                                                  |
    | [2]  is_valid_category(query)  : checks if the given query is defined in the categories.                                         |
    |                                                                                                                                  |
    | [3]  find_subcategories(query) : returns a list containing the query category and all the subcategories under it (if any).       |
    ====================================================================================================================================
    '''
    
    def __init__(self):
        '''
        ================================================================================================================================
        | The constructor of the Categories class.                                                                                     |
        ================================================================================================================================
        '''
        self._category = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway'], 'entertainment', ['movie', 'concert'], 'other_expenses'], \
                          'income',  ['salary', 'bonus', 'other_incomes'], 'miscellaneous']

    
    def view(self):
        '''
        ================================================================================================================================
        | view is a method that prints out a comprehensive and indented list of the categories.                                        |
        ================================================================================================================================
        '''
        def _recursive_view(L, prefix = -1):
            if(type(L) == str):
                print('\t' + '|⎯⎯⎯⎯⎯⎯⎯⎯' * prefix + '|⎯+ ' + L.capitalize())
            else:
                for elem in L:
                    _recursive_view(elem, prefix + 1)
            
        _recursive_view(self._category)
        
    def is_valid_category(self, query):
        '''
        =================================================================================================================================
        | is_valid_category is a method that checks if the given query is defined in the categories.                                    |
        |                                                                                                                               |
        | Required formal parameter:                                                                                                    |
        | [1] query : the target category to find, in string                                                                            |
        =================================================================================================================================
        '''
        
        # A recursive find inner function
        def recursive_find_category(L, query):
            return (type(L) == list) and any((query == elem or recursive_find_category(elem, query)) for elem in L)
        
        return recursive_find_category(self._category, query.lower())
        
    def find_subcategories(self, query):
        '''
        =================================================================================================================================
        | find_subcategories is a method that returns a list containing the query category and all the subcategories under it (if any). |
        |                                                                                                                               |
        | Required formal parameter:                                                                                                    |
        | [1] query : the target category to find, in string                                                                            |
        =================================================================================================================================
        '''
        
        query = query.lower()
        
        # A generator as an inner function
        def subcategories_generator(L, query, found = False):
            if (type(L) == list):
                for index, elem in enumerate(L):
                    yield from subcategories_generator(elem, query, found)
                    if (elem == query) and (index + 1 < len(L)) and (type(L[index + 1]) == list):
                        yield from subcategories_generator(L[index + 1], query, found = True)
            else:
                if found or (query == L):
                    yield L
        
        return [i for i in subcategories_generator(self._category, query)]
    
class Record:
    '''
    ====================================================================================================================================
    |                                                                                                                                  |
    | Record is a class that maintains a singular record, i.e. its category, name, and amount of money.                                |
    |                                                                                                                                  | 
    ====================================================================================================================================
    | Available usable methods and their purposes:                                                                                     |
    ====================================================================================================================================
    | [1]  summary                   : returns a tuple of three elements: its category, name, and amount of money.                     |
    |                                                                                                                                  |
    | [2]  category                  : returns a record's category.                                                                    |
    |                                                                                                                                  |
    | [3]  name                      : returns a record's name.                                                                        |
    |                                                                                                                                  |
    | [4]  amount                    : returns a record's amount of money.                                                             |
    ====================================================================================================================================
    '''
    def __init__(self, category = 'miscellaneous', name = 'Unspecified', amount = 0):
        '''
        ================================================================================================================================
        | The constructor of the Record class.                                                                                         |
        |                                                                                                                              |
        | Optional formal parameters:                                                                                                  |
        | [1] category : the category, that this record belongs to, in string                                                          |
        | [2] name     : the record name in string                                                                                     |
        | [3] amount   : the amount of money this record in integer or float                                                           |
        ================================================================================================================================
        '''
        if(type(category) != str): 
            sys.stderr.write('[TypeError] Passed parameter category is not a string.\n')
            sys.stderr.write('[Quick fix] Changed category into \'miscellaneous.\'\n\n')
            category = 'Unspecified'
            
        if(type(name) != str):
            sys.stderr.write('[TypeError] Passed parameter name is not a string.\n')
            sys.stderr.write('[Quick fix] Changed name into \'Unspecified.\'\n\n')
            name = 'Unspecified'
            
        if(type(amount) not in {int, float}):
            sys.stderr.write('[TypeError] Passed parameter amount is not an integer nor a float.\n')
            sys.stderr.write('[Quick fix] Changed amount into 0.\n\n')
            amount = 0
            
        self._category = category
        self._name     = name
        self._amount   = amount
    
    def __bool__(self):
        '''
        ================================================================================================================================
        | A bool representation of the Record class.                                                                                   |
        | False if all its value is the default value. True otherwise.                                                                 |
        ================================================================================================================================
        '''
        return ((self.category == 'miscellaneous') and (self.name == 'Unspecified') and (self.amount == 0))
    
    def __repr__(self):
        '''
        ================================================================================================================================
        | A representation of the Record class.                                                                                        |
        ================================================================================================================================
        '''
        return f'Record({self.category}, {self.name}, {self.amount})'
    
    def __str__(self):
        '''
        ================================================================================================================================
        | A string representation of the Record class.                                                                                        |
        ================================================================================================================================
        '''
        return f'{self.category:s} {self.name:s} {self.amount:d}'
    
    @property
    def category(self):
        '''
        ================================================================================================================================
        | A derived attribute that returns a record's category.                                                                        |
        ================================================================================================================================
        '''
        return self._category
    
    @property
    def name(self):
        '''
        ================================================================================================================================
        | A derived attribute that returns a record's name.                                                                            |
        ================================================================================================================================
        '''
        return self._name
    
    @property
    def amount(self):
        '''
        ================================================================================================================================
        | A derived attribute that returns a record's amount of money.                                                                  |
        ================================================================================================================================
        '''
        return self._amount
    
    @property
    def summary(self):
        '''
        ================================================================================================================================
        | A derived attribute that returns a tuple of three elements: its category, name, and amount of money.                         |
        ================================================================================================================================
        '''
        return (self.category, self.name, self.amount)

class Records:
    '''
    ====================================================================================================================================
    |                                                                                                                                  |
    | Records is a class that maintains a collection of records and inital amount of money.                                            |
    |                                                                                                                                  | 
    ====================================================================================================================================
    | Available usable methods and their purposes:                                                                                     |
    ====================================================================================================================================
    | [1]  add                   : adds a (series of) new record(s) into the record list.                                              |
    |                                                                                                                                  |
    | [2]  view                  : prints out the existing record(s) in the record list.                                               |
    |                                                                                                                                  |
    | [3]  delete                : deletes a (series of) specified record(s) in the record list.                                       |
    |                                                                                                                                  |
    | [4]  find                  : prints out existing records(s) with the given categories.                                           |
    |                                                                                                                                  |
    | [5]  save                  : saves and exports existing record(s) into a file.                                                   |
    ====================================================================================================================================
    '''
    def __init__(self, filename = 'records.txt'):
        '''
        ================================================================================================================================
        | The constructor of the Records class.                                                                                        |
        |                                                                                                                              |
        | Optional parameter:                                                                                                          |
        | [1] filename : the file name that the record is stored in or to be stored at.                                                |
        |                By default, filename is 'records.txt'                                                                         |
        ================================================================================================================================
        '''
        self._filename      = filename
        self._initial_money = 0
        self._records       = []

        completion_flag = False

        while not completion_flag:

            try:
                with open(self._filename, 'r') as ifstream:

                    try:
                        # Read in the initial amount of money
                        self._initial_money = int(ifstream.readline())

                    except ValueError:
                        sys.stderr.write('[ValueError] Initial amount of money cannot be converted into integer with base 10.\n')
                        sys.stderr.write('[Quick fix]  Initial amount of money overwritten as $0\n\n')

                        initial_money = 0

                    # Read all remaining lines in records.txt
                    records_list = ifstream.readlines()

                    # Consequently, convert the remaining records in the file into list of triplets (record category, record name, amount)
                    for line in records_list:

                        triplet = line.split()

                        # An unacceptable format of record, skip
                        if(len(triplet) != 3):
                            sys.stderr.write(f'[Unrecognized Record] The record \'{line[:-1]}\' is in an incorrect format.\n')
                            sys.stderr.write(f'[Quick fix]           The record has been ignored.\n\n')
                            continue

                        try:
                            record_category = triplet[0]
                            record_name     = triplet[1]
                            record_amt      = int(triplet[2])

                        except ValueError:
                            sys.stderr.write(f'[ValueError] The amount of money in record \'{line[:-1]}\' cannot be converted into integer with base 10.\n')
                            sys.stderr.write(f'[Quick fix]  The amount of money in the record is parsed as $0\n\n')

                            record_amt = 0

                        # Place the record into 
                        self._records.append(Record(record_category, record_name, record_amt))

                # Ends without error: file parsing complete
                completion_flag = True


            # No old records can be found. Prompt user for initial amount of money
            except FileNotFoundError:

                print('\tNo old records can be found. Please make new record with the following step.\n\n')

                # Repeat until users input an integer
                while True:
                    try:
                        self._initial_money = int(input('\tPlease input the initial starting amount of money: '))
                    except ValueError:
                        print('[ValueError] Your input cannot be converted into integer with base 10.')
                    else:
                        break

                print('\tNew record created! Thank you very much.\n\n\n')

                # Ends without error: file parsing complete
                completion_flag = True

            # Does not have access to records.txt.
            except PermissionError:

                sys.stderr.write('[PermissionError] records.txt cannot be opened.\n')
                sys.stderr.write('[Quick fix]       Attempting to unlock permission...\n\n')

                # Unlock restriction
                os.chmod('records.txt', stat.S_IREAD | stat.S_IWRITE)

                # Repeat the while loop
                continue

    def __len__(self):
        '''
        ================================================================================================================================
        | The length representation of the Records class.                                                                              |
        | This returns the length of the list that contains the existing records                                                       |
        ================================================================================================================================
        '''
        return len(self._records)
    
    def add(self, categories, processed_record):
        '''
        ================================================================================================================================
        | add is a method that appends a list of new record(s) into the list of existing records.                                      |
        |                                                                                                                              |
        | Required formal parameters:                                                                                                  |
        | [1] categories      : a Categories instance that contain a predefined list of categories.                                    |
        | [2] processed_record: a list containing Record instance(s)                                                                   |
        |                                                                                                                              |
        | Any new record in processed record which category not belonging to the predefined categories will be maintained with the     |
        | following strategy:                                                                                                          |
        | [1] If the record has negative amount, its category will be labelled 'Other_expenses'                                        |
        | [2] If the record has positive amount, its category will be labelled 'Other_incomes'                                         |
        | [3] If the record has zero amount, its category will be labelled 'Miscellaneous'                                             |
        ================================================================================================================================
        '''
        # Check for every triplets that the first element (its category) exists in the predefined categories
        for record in processed_record:
            if(not categories.is_valid_category(record.category)):
                sys.stderr.write(f'[Unrecognized Category] the record {str(record)} does not belong to any predefined categories.\n')
                
                # If the record has negative value, then it has to be an expense
                if(record.amount < 0):
                    record._category = 'other_expenses'
                    sys.stderr.write( '[Quick fix]             The record has been stored as \'Other_expenses\'\n\n')
                
                # If the record has positive value, then it has to be an income
                elif(record.amount > 0):
                    record._category = 'other_incomes'
                    sys.stderr.write( '[Quick fix]             The record has been stored as \'Other_incomes\'\n\n')
                
                # If the record has the value zero, then it has to be a miscellaneous log
                else:
                    record._category = 'miscellaneous'
                    sys.stderr.write( '[Quick fix]             The record has been stored as \'Miscellaneous\'\n\n')
                
                self._records.append(record)
                continue
            
            self._records.append(record)
            
    def view(self, filter_func = lambda pair: pair, show_header = True):
        '''
        ================================================================================================================================
        | view is a method that displays the existing record list.                                                                     |
        |                                                                                                                              |
        | Optional formal parameters:                                                                                                  |                                                         
        | [1] filter_func : A function that takes in a tuple of (index, record) in the existing record list.                           |
        |                   By default, filter_func returns True to all tuples of (index, record)                                      |
        | [2] show_header : A bool flag that allows the header and initial amount of money to be shown if it is True.                  |
        |                   By default, show_header is True                                                                            |
        ================================================================================================================================
        '''
        print('\t' + '_' * 72)
        
        if(show_header):
            # Print header
            print('\t|' + '-' * 70 + '|')
            print('\t|{:-^70s}'.format('RECORD') + '|')
            print('\t|' + '-' * 70 + '|')
            print('\t|' + ' ' * 70 + '|')

            # Print intial money
            print('\t|      {:40s} : ${:20d}|'.format('Initial Money', self._initial_money))
            print('\t|' + '-' * 70 + '|')
            print('\t|' + '-' * 70 + '|')
            
        print(f"\t|{'idx':3s} | {'Category':^19s}|{'Name':^20s} | {'Amount':^21s}|")
        print('\t|' + ' ' * 4  + '|' + ' ' * 20 + '|' + ' ' * 21 + '|' + ' ' * 22 + '|')
        print('\t|' + ' ' * 4  + '|' + ' ' * 20 + '|' + ' ' * 21 + '|' + ' ' * 22 + '|')

        # Print records while summing the total
        total = self._initial_money if show_header else 0
        for (i, record) in enumerate(self._records):
            
            if not filter_func((i, record)):
                continue
            
            print(f'\t|{(i+1):03d} | {record.category.capitalize():19s}| {record.name:19s} | ${record.amount:20d}|')

            total += record.amount

        print('\t|' + '-' * 70 + '|')
        print('\t|' + ' ' * 70 + '|')

        # Print total
        print('\t|      {:40s} : ${:20d}|'.format('Balance' if show_header else 'Total', total))
        print('\t|' + '_' * 70 + '|\n\n')
        
    def delete(self, index_list):
        '''
        ================================================================================================================================
        | delete is a method that deletes the existing records with index in the passed index list.                                    |
        |                                                                                                                              |
        | Required formal parameters:                                                                                                  |                                                         
        | [1] index_list : a list of integers specifying the indicies of records to be removed.                                        |
        ================================================================================================================================
        '''
        new_records = []
        for (i, record) in enumerate(self._records):
            
            # Assuming the index list is sorted, it behaves like a queue.
            # Hence, we can sequentially decide which item to not add into the new list by looking at the front of index list.
            if((index_list == []) or (i != index_list[0])):
                new_records.append(record)
                continue
            
            # If the current index i matches the front of the index list, remove the current record.
            index_list.pop(0)
        
        self._records = new_records
    
    def find(self, category_list):
        '''
        ================================================================================================================================
        | find is a method that displays the existing records with categories in the passed category list                              |
        |                                                                                                                              |
        | Required formal parameters:                                                                                                  |                                                         
        | [1] category_list : a list of categories in string specifying which records to be displayed                                  |
        ================================================================================================================================
        '''
        self.view(filter_func = lambda pair: (pair[1].category in category_list), show_header = False)
        
    def save(self):
        '''
        ================================================================================================================================
        | save is a method that saves the initial amount of money and existing records into the file.                                  |
        ================================================================================================================================
        '''
        completion_flag = False

        while not completion_flag:

            try:
                # Open the file with overwrite option
                # Reason 1: We may had encountered records with incorrect mode. This is a chance to remove them.
                # Reason 2: Simplicity, might need to avoid repetition with append mode.  
                with open(self._filename, 'w') as ofstream:

                    # First, write the initial_money
                    ofstream.write(str(self._initial_money) + '\n')

                    # Second, write the records into a buffer (list of strings)
                    buffer = []
                    for record in self._records:
                        buffer.append(str(record) + '\n')

                    # Third, write buffer into records.txt
                    ofstream.writelines(buffer)

                # Ends without error: complete
                completion_flag = True

            # Do not have permission to records.txt
            except PermissionError:

                sys.stderr.write('[PermissionError] records.txt cannot be opened.\n')
                sys.stderr.write('[Quick fix]       Attempting to unlock permission...\n\n')

                # Unlock restriction
                os.chmod(self._filename, stat.S_IREAD | stat.S_IWRITE)

                # Repeat while loop
                continue

def preprocess_added_records(input_str):
    '''
    ================================================================================================================================
    | preprocess_added_records is a function that preprocesses the input string by the user into a list of Record instances.       |
    |                                                                                                                              |
    | If the record is lacking any element, i.e. not in three (category, name, amount of money), ignore this record.               |
    | If the record only has an ill-defined amount of money, i.e. amount of money in string, prompt user to correct it.            |
    |                                                                                                                              |
    | Returns a list of Record instances.                                                                                          |
    ================================================================================================================================
    '''
    # First, split input by ',', then ' ' (might need to remove residual ' ')
    input_records = input_str.split(',')
    new_records_list = []
    for record in input_records:
        temp_list = record.split(' ')

        # Remove the residual '' at front of the records (if exists)
        if(temp_list and (temp_list[0] == '')):
            temp_list.pop(0)

        new_records_list.append(temp_list)

    processed_record_list = []
    # Second, parse every (category, name, amount) pair and append to each record as an instance of Record.
    for triplet in new_records_list:

        if(len(triplet) != 3):
            sys.stderr.write(f'[Unrecognized record] The record \'{triplet}\' is in an unrecognized format.\n')
            sys.stderr.write('[Quick fix]           The record has been ignored.\n\n')
            continue

        valid_flag = False
        while not valid_flag:
            try:
                triplet[2] = int(triplet[2])

                valid_flag = True

            except ValueError:
                sys.stderr.write(f"[Unrecognized record] The amount value of record \'{str(triplet[0]) + ' ' + str(triplet[1])}\' cannot be converted to an integer of base 10.\n")
                sys.stderr.write('[Quick fix]           Prompt user again.\n\n')

                triplet[2] = input(f"\tFor record \'{str(triplet[0]) + ' ' + str(triplet[1])}\',\n\tPlease input its amount: ")
                continue

        processed_record_list.append(Record(triplet[0].lower(), triplet[1], triplet[2]))
    
    return processed_record_list

def preprocess_deleted_records(input_idx, upperbound):
    '''
    ================================================================================================================================
    | preprocess_deleted_records is a function that preprocesses the input string by the user into a list of legal indexes.        |
    |                                                                                                                              |
    | If any index in the list is an index that is below 0 or exceeds the index of existing records, ignore it.                    |
    | If any index in the list is a duplicate of other index in the list, remove duplicates.                                       |
    |                                                                                                                              |
    | Returns a list of unique, sorted, and legal indices.                                                                         |
    ================================================================================================================================
    '''
    
    # Filter for incompatible type
    for i in range(len(input_idx)):
        # If cannot convert, throw a ValueError exception that will be caught in the caller
        input_idx[i] = int(input_idx[i]) - 1
    
    # Filter legal indices
    legal = []
    for index in input_idx:

        if((index < 0) or (index >= upperbound)):
            sys.stderr.write(f'[IndexError] The index {index + 1} is out of bound.\n')
            sys.stderr.write(f'[Quick fix]  The index has been ignored.\n\n')
            continue

        legal.append(index)

    # Sort indices
    legal = sorted([i for i in {i for i in legal}])
    return legal

if __name__ == '__main__':

    records    = Records()
    categories = Categories()
    
    os.system('clear')
    
    # Constant string literal`
    display_text = '''
        Instructions menu:

        [*] add      : Add record(s)
        [*] view     : View existing record(s)
        [*] delete   : Delete a record
        [*] view_cat : View categories
        [*] find     : View existing record(s) under a category
        [*] exit     : Save existing record(s) and quit program
    
        What do you want to do? '''

    print('\tHere is a summary of previous record.\n')
    records.view()
    input('\tPress ENTER to continue...')
    
    while True:
        
        os.system('clear')
        command = input(display_text).lower()
        
        # Add record(s)
        if(command == 'add'):
            print('\tAdd some expense or income records with description and amount with the format:')
            print('\tcat_1 desc_1 amount_1, cat_2 desc_2 amount_2, cat_3 desc_3 amount_3, ...\n')
            records.add(categories, preprocess_added_records(input('\tRecords: ')))

            print('\n\tAdding record(s) successful!\n\tReturning...\n\n')
            
        # View records
        elif(command == 'view'):
            records.view()
            input('\n\tPress ENTER to continue...')
        
        # Delete record(s)
        elif(command == 'delete'):
            records.view(show_header = False)

            # Secondly, prompt the user for the indices of the records they want to delete
            while True:
                try:
                    print('\tEnter the indices of the records you wish to delete in the format: index_1 index_2 index_3 ...')
                    processed_index_list = preprocess_deleted_records(input('\tIndices: ').split(' '), len(records))
                    
                # Catches ValueError when user inputs an index with ill-defined format (i.e. string)
                except ValueError:
                    sys.stderr.write('[ValueError] Please follow the correct format: index_1 index_2 index_3 ...\n')
                    sys.stderr.write('[Quick fix]  Prompting user for input.\n\n')
                    continue
                else:
                    break
            
            # If the index list is empty, abort early
            if(processed_index_list == []):
                print('\n\tThere is nothing to delete, returning...\n\n')
                time.sleep(2)
                continue

            # Third, reconfirm with user that these records are going to be deleted permanently
            print('\n\tThese records are going to be deleted:')
            records.view(filter_func = lambda pair: (pair[0] in processed_index_list), show_header = False)

            # If the user is sure, delete all the specified records
            if(input('\tPress Y if you are sure. Otherwise, press any other key to cancel deletion ').lower() == 'y'):
                records.delete(processed_index_list)
                print('\n\tRecords deleted successfully!\n\tReturning...\n\n')
            else:
                print('\tDelete aborted.\n\n')
        
        # View categories
        elif(command == 'view_cat'):
            
            print('\n\tCategory')
            categories.view()
            
            input('\n\n\tPress ENTER to continue...')
            print('\tReturning...\n\n')
            
        # Find record(s) under a category
        elif(command == 'find'):
            
            # Get the category to find
            query = input('\n\tEnter the category to find: ').split(' ')
            
            if(query == [''] or not categories.is_valid_category(query[0])):
                print('\tYou have not input any valid category. There is nothing to show. Returning...\n\n')
                time.sleep(2)
                continue
            if(len(query) > 1):
                print(f'\tWARNING: You entered more than one category, only {query[0]} will be considered.\n')
            
            records.find(categories.find_subcategories(query[0]))
            
            input('\tPress ENTER to continue...')
            print('\tReturning...\n\n')
        
        elif(command == 'exit'):
            break
        
        else:
            print('\tUnrecognized command. Try again...\n\n')
        
        time.sleep(2)
    
    records.save()
    print(f'\n\n\tRecords saved into {str(records._filename)} successfully!')
    print(f'\tPyMoney terminating. Looking forward to see you again!\n\n')