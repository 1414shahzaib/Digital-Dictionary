def index( character):
        alphabet_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","n",\
            "o","p","q","r","s","t","u","v","w","x","y","z"]
        for alpha in (alphabet_list):
            if character==alpha:
                index=alphabet_list.index(alpha)
                return index
        #print(ord(character)-ord("a"))   

print(index("z"))                                                                                                                           
