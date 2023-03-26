kata = (0, 9, 25, 3, 30)

# create new tuple that loops into kata
# first convert items into string (str(num))
# then check if length of string is 1 
# if it is, prepend a zero until it reaches the speciified length (4 if i == 0 et 2 sinon) (.zfil(digits))
# if not 1, simply return as it is
import sys
def contains_only_integers(kata):
    for item in kata:
        if not isinstance(item, int) or item < 0 :
            print("Erreur")
            sys.exit()
# new_kata = tuple(str(num).zfill(4) if i == 0 else str(num).zfill(2) if len(str(num)) < 2 else str(num) for i, num in enumerate(kata))

    tablo = []
    for i, num in enumerate(kata):
        if i == 0:
            var1 = str(num).zfill(4)  
            tablo.append(var1)
        else:
            var2 = str(num).zfill(2) 
            tablo.append(var2)
    print('{}\\{}\\{} {}:{}'.format(tablo[1], tablo[2], tablo[0], tablo[3], tablo[4]))


    sys.exit()


contains_only_integers(kata)

# total_size = len(new_kata)
# first_number = new_kata[0]
# second_number = new_kata[1]
# third_number = new_kata[2]
# fourth_number = new_kata[3]
# fifth_number = new_kata[4]

# print('{}\\{}\\{} {}:{}'.format(second_number, third_number, first_number, fourth_number, fifth_number)) 