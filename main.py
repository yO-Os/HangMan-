
import random 

words = ['elite','event','cats','deep','smooth','ring','clear','drawer']    

number = int(random.random()*len(words))



count = 0

def pickword():
    pickedword = words[number]
    return pickedword
def dash():
    guessed = []
    for x in range(0,len(pickword())):
        print("_", end=' ')
        
        # guessed[x] = ['_']
        if pickword()[x] == userinput:
                guessed[x] = userinput
        else: count+=1
        return guessed

print(dash())

userinput = input("guess a character")
chances=0
def check():
    picked_word=''
    letter=''
    while(chances<6):
       latter=input("Enter a character")
        
        