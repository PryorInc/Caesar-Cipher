alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypt = " "

def removeNonAlphas(inputstring):
    outstring = ""
    for lett in inputstring:
        if lett.upper() in alphabet:
            outstring += lett.upper()
    return outstring

def rot_encrypt(plaintext, rot):
    rotation = int(rot)
    outtext = ""
    for lett in plaintext:
        if lett in alphabet:
            outtext += alphabet[(alphabet.index(lett) + rotation)%26]
    return outtext
    




while (not encrypt in "DE"):
    encrypt = input("Do you want to [E]ncrypt or [D]ecrypt (choose a letter)? ").upper()

if encrypt == "E":
    userinput = input("What do you want to encrypt? ")
    rotation = input("What rotation do you want to use? ")
else:
    userinput = input("What would you like to decrypt? ")
    
if len(userinput) > 0:
    inputtext = removeNonAlphas(userinput)

else:
    print ("You must enter text!")
    
outtext = rot_encrypt(inputtext,rotation) if encrypt == "E" else rot_decrypt(inputtext,userpw,True)

print (inputtext," => ",outtext)

