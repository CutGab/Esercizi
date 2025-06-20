from string import ascii_lowercase

def encrypt (s: str, key: int) -> None:
    
    encrypted_s: str =  ""
    
    for element in s.lower():

        if element in ascii_lowercase:
            
            encrypted_s += ascii_lowercase[ascii_lowercase.index(element) + key]

        else:

            encrypted_s += element

    return encrypted_s

def decrypt (s: str, key: int) -> None:
    
    encrypted_s: str =  ""
    
    for element in s.lower():

        if element in ascii_lowercase:
            
            encrypted_s += ascii_lowercase[ascii_lowercase.index(element) - key]

        else:

            encrypted_s += element

    return encrypted_s

print(encrypt("CIAO A TUTTI!", 3)) #fldr d wxwwl!
print(decrypt("FLDR D WXWWL!", 3)) #ciao a tutti!




        

