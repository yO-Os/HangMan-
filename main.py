
import random 

words = ['elite','event','cats','deep','smooth','ring','clear','drawer']    

number = int(random.random()*len(words))
userinput = 'w'

guessed = []

def pickword():
    pickedword = words[number]
    return pickedword
def dash():
    count = 0
    for x in range(0,len(pickword())):
        guessed.append('_')

dash()
print(pickword())
print(guessed)


def check():
    chances=0
    while(chances<6):
       userinput = input("guess a character")
       
       count=0
       for x in range(0,len(pickword())):
          if(pickword()[x]==userinput):
              guessed[x]=userinput
          else:
              count+=1
       if(count==len(pickword())):
           chances+=1
       print(f'{guessed} chances: {6-chances}')   
check()