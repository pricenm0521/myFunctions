# functions.py

def print_even(num):
    '''
    Print even numbers from 2 to num
    :param num: upper limit of processing
    '''
    for i in range(num):
        if (i % 2 == 0):
            print (i)

# write a function that converts a string passed as a parameter to all upper case
# and returns the converted string

def convert(some_string):
    '''
    Convert a string to upper case and return the string
    :param some_string: the string to convert
    '''
    return some_string.upper()