import sys

def text_analyzer (sglstring):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    
    # for i in range (0, n):


    if not isinstance(sglstring, str):
        print("erreur")
        sys.exit()
    n = len(sglstring)

    if n == 0:
        sglstring = input("Donne moi un string stp: ")
        n = len(sglstring)
    
    space = 0
    uplet = 0
    lowlet = 0
    punct = 0
    for i in range (0, n):

        if sglstring[i].isdecimal() == True:
            continue
        if sglstring[i] == ' ':
            space = space + 1
        elif sglstring[i].isalpha() == True:
           
            if sglstring[i].isupper() == True:
                uplet = uplet + 1

            elif sglstring[i].islower() == True:
                lowlet = lowlet + 1
                
        else:
            punct = punct + 1


    print('The text contains {} character(s):\n -{} upper letter(s)\n -{} lower letter(s) \n -{} punctuation mark(s)\n -{} space(s).'.format(n, uplet, lowlet, punct, space) )

if len(sys.argv) == 2:    
    sexystring = sys.argv[1]
    text_analyzer(sexystring)  
    
elif len(sys.argv) == 1:
    
    text_analyzer(str())       
else:
    print("Erreur")
# if n == 1:
    #   print()
# for i in range (1, n):
        # print(n)
        # textimp = text_analyzer(str(arg[i]))
        # print (textimp, end = " ")
        
