

import sys
def cal_two_numbers (A, B):
    sum = A + B
    dif = A - B
    prod = A * B
    quot = 'lquotpapossib'
    rem = 'lrempapossib' 
    if B != 0:
        quot = A / B
        rem = A % B 
    print('Sum:        {} \nDifference: {} \nProduct:    {}\nQuotient:   {}\nRemainder:  {}'.format(sum, dif, prod, quot, rem) )

if len(sys.argv) == 3:    
    premier_argument = sys.argv[1]
    deuxieme_argument= sys.argv[2]
    if premier_argument.isdecimal() == True and deuxieme_argument.isdecimal() == True:
        print("ok")
    else:
        print("nonmerci")
        sys.exit()
    cal_two_numbers(int(sys.argv[1]), int(sys.argv[2]))
        
      
else:
    print("Erreur")

