
def decrypt(message,shifts): 

    final=""
        
    for characters in message:
        initial= ord(characters)- ord("A")
        new=(initial - shifts) % 26
        final+= chr(new+ord("A"))
        
    return final
    
    

while True:

        print("Welcome to the Secret Message Decoder!")
        print("Type 'exit' to stop.")
        print()
        print("Select mode:")
        selection=input("1. Encryption \n2. Decryption\n").lower()


        if selection in ["encryption","1","encrypt"]:

            while True:
                try:
                    message=input("Word:").upper()
                    if message == "EXIT":
                        break
                    shifts=int(input("Number of shifts:"))
                    print()
                except ValueError:
                    print("Invalid input.")
                    continue

                     
                if message.isalpha():

                    encrypted=""

                    for characters in message:

                        new=ord(characters) - ord("A")
                        new2= (new+shifts) % 26
                        encrypted= encrypted + chr(new2 + ord("A"))
                        final=encrypted.capitalize()

                    print("Encrypted message:", final)
                    print()
                    break

                else:
                    print("PLease enter an alphabetic message")
                    continue

        elif selection in ["decryption","2","decrypt"]:

            while True:
                    
                        message=input("Encrypted word:").upper()
                        print()

                        if message=="EXIT":
                            break
                        elif message.isalpha(): 
                            print("Listing 25 possible combinations:")
                            for shifts in range(0,26):
                                print(shifts, decrypt(message, shifts).capitalize())
                        else:
                            print("Please enter an alphabetical message.")
        
        elif selection in ["exit","quit"]:
             break
        
        else:
            print("Invalid input.\n")
            continue