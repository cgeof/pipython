# A dictionary is a collection of unordered,
# modifiable(mutable) paired (key: value) data type.
import sys

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def contains_only_str(kata):
    for item in kata:
        if not isinstance(item, str):
            print("not str in the tuple")
            sys.exit()
    # key_1 = [key for key in kata.keys()][0]
    # key_2 = [key for key in kata.keys()][1]
    # key_3 = [key for key in kata.keys()][2]
    # val_1 = [value for value in kata.values()][0]
    # val_2 = [value for value in kata.values()][1]
    # val_3 = [value for value in kata.values()][2]
    # val_1 = kata['Python']
    # val_2 = kata['Ruby']
    # val_3 = kata['PHP']
    # print('{} was created by {}\n{} was created by {}\n{} was created by {}'.format(key_1, val_1, key_2, val_2, key_3, val_3))

    # 2eme méthode en 1 ligne
    # print('-'*8)
    print('\n'.join(str(key) + ' was created by ' + str(value) for key, value in kata.items()))


contains_only_str(kata)