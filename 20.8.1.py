string="ahsdubqubcbwirvnjqwvnqqefgjbiewfhbvjvnkewnfvh"
find_list=["a","b","c","d","e","f","g","h","i","j"
           ,"k","l","m","n","o","p","q","r","s","t"
           ,"u","v","w","x","y","z"]

def count_alphabet(string,character):
    count=0
    for letter in string:
        if letter.lower()==character.lower():
            count+=1
    return count

for letter in find_list:
    n=count_alphabet(string,letter)
    if n>0:
        print("{0} {1}".format(letter,n))
  
    
