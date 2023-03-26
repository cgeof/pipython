
import sys

# A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, ().
# Once a tuple is created, we cannot change its values. 
# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple 

# tuple with initial values
kata = (9, 42, 21)

def contains_only_integers(kata):
    for item in kata:
        if not isinstance(item, int):
            print("not integer in the tuple")
            sys.exit()
        
    total_size = len(kata)
    tous_les_katas = kata[0:]
    format = str(tous_les_katas)
    format = format.replace( '(', '')
    format = format.replace( ')', '')


    print('The {} numbers are: {}'.format(total_size, format)) 

contains_only_integers(kata)