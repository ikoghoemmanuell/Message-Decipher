import os
import platform

#create string for all letters
plain='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalPositions=len(plain)

#create myFunction 
def myFunction():
    #create encription function to accept message and print coded message
    def encriptMessage():
        encripted=''
        #ask the user for a message
        message=input('Type a message that you want to encript: ').upper()
        shift=int(input(f'How many shifts to the right(1-{totalPositions}): '))
        for letter in message:
            if letter in plain:
                position=plain.index(letter)+shift
                if position>totalPositions-1:
                    encripted+=plain[position-totalPositions]
                else:encripted+=plain[position]
            else:
                encripted+=letter
        print(f'Your encripted message: {encripted}')        

    #create decription function to accept coded message and print original message
    def decriptMessage():
        decripted=''
        #ask the user for a message
        message=input('Type a message that you want to decript: ').upper()
        shift=int(input(f'How many shifts to the right was your encription(1-{totalPositions}): '))
        for letter in message:
            if letter in plain:
                position=plain.index(letter)-shift
                if position>totalPositions+1:
                    decripted+=plain[position+totalPositions]
                else:decripted+=plain[position]
            else:
                decripted+=letter
        print(f'Your original message: {decripted}')        

    #ask user if encrypt or decript
    choice=input('encript or decript? ').lower()
    if choice=='encript':
        encriptMessage()
    elif choice=='decript':
        decriptMessage()
    else:
        print('wrong! (encript/decript)')

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
