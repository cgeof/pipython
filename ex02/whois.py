import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for arg in sys.argv[1:]:
    if not is_intstring(arg):
        sys.exit("AssertionError: not integer")

n = len(sys.argv)    
if n == 0:
      print()
if n == 2:
    nb = int(sys.argv[1])

    if nb == 0:
        print ("I'm zero")
        
    if nb > 0 and nb % 2 == 0:
        print ("I'm Even")
        
    if nb > 0 and nb % 2 != 0:
        print ("I'm Odd")
        
for arg in sys.argv[1:]:
    if n>2:
        sys.exit("AssertionError: more than one argument are provided")



