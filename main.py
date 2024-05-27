
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


while count < 5:
    userinput = input("guess a character")
    print(dash())
    

