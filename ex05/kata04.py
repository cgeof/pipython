kata = (0, 4, 132.422222, 10000, 12345.67)

import sys
from decimal import Decimal
import math

def contains_only_integers(kata):
    tablo = []
    for i, num in enumerate(kata):
        if i == 0 or i == 1 and isinstance(num, int) and num >= 0:
            var1 = str(num).zfill(2)  
            tablo.append(var1)
        if i == 2 and isinstance(num, float):
            var2 = round(num,2) 
            tablo.append(var2)
        if i == 3 and isinstance(num, int):
            var3 = str(num) 
            var3 = "{:.2e}".format(num)
            tablo.append(var3)
        if i == 4 and isinstance(num, float):
            var4 = str(num) 
            var4 = "{:.2e}".format(num)
            tablo.append(var4)
    print('module_{}, ex_{}: {}, {}, {}'.format(tablo[0], tablo[1], tablo[2], tablo[3], tablo[4]))


    sys.exit()

    
contains_only_integers(kata)
