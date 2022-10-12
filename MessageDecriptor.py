import os
import platform

#create string for all letters
plain='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cypher='XYZABCDEFGHIJKLMNOPQRSTUVW'

#create myFunction 
def myFunction():
    #display options (encrypt and decript)
    print('\n1. Decript \n2. Encript')

    #create decription function to accept coded message and print original message
    def deCript(message):
        deCodedText=''
        for letter in message.upper():
            if letter in cypher:
                deCodedText+=plain[cypher.index(letter)]
            else: 
                deCodedText+=letter
        print(f'original message is: {deCodedText}')

    #create encription function to accept message and print coded message
    def enCript(message):
        codedText=''
        for letter in message.upper():
            if letter in plain:
                codedText+=cypher[plain.index(letter)]
            else: 
                codedText+=letter
        print(f'coded message is: {codedText}')

    #ask the user to choose decript or encript
    choice=input('Pick 1 or 2: ').lower()

    #decode or encript based on user's choice 
    if choice=='1':
        deCript(input('\nEnter Coded Message: '))
    elif choice=='2':
        enCript(input('\nEnter Original Message: '))
    else:
        print('Wrong! (1/2)')

#repeat the program if user says yes
def runAgain():
    run=input('\nGo again? Y/n: ').lower()
    if run=='y':
        if(platform.system()=='Windows'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        myFunction()
        runAgain()

    else: 
        print('HAVE A NICE DAY')

myFunction()
runAgain()
