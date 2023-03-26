# string.swapcase() 
import sys

def rev(str):
    tablo = str.split(' ')
    tablo2 = ' '.join(tablo)
    stv = tablo2.swapcase()
    stu = stv[::-1]
    
    return(stu)

n = len(sys.argv)

if n == 1:
      print()
while n > 1:
    
        print (rev(str(sys.argv[n-1])), end = " ")
        n= n-1
   

# revalpha("Hello" "my friend")
# revalpha("")   
# str = str.split()
# stv = str.swapcase()