
import random 


words = ['elite','event','cats','deep','smooth','ring','clear','drawer']    

number = int(random.random()*len(words))



def pickword():
    pickedword = words[number]
    return pickedword
def dash():
    for x in range(0,len(pickword())+1):
        print("_")

# print("HangMan")

print(dash())

userinput = input("guess a character")
