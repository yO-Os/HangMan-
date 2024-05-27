
import random 

words = ['elite','event','cats','deep','smooth','ring','clear','drawer']    

number = int(random.random()*len(words))
userinput = 'w'
guessed = []
won=False

def pickword():
    pickedword = words[number]
    return pickedword
def dash():
    pickword()
    count = 0
    for x in range(0,len(pickword())):
        guessed.append('_')
def full():
    count=0
    for x in range(0,len(pickword())):
        if(guessed[x]!='_'):
            count+=1
    return count
dash()
print(guessed)
def check():
    global won
    chances=0
    while(chances<6):
       userinput = input("guess a character: ")     
       count=0
       for x in range(0,len(pickword())):
          if(pickword()[x]==userinput):
              guessed[x]=userinput
          else:
              count+=1
       if(count==len(pickword())):
           chances+=1
       if(full()==len(pickword())):
           print(f'{guessed} chances: {6-chances}')
           chances=6
           won=True
       print(f'{guessed} chances: {6-chances}')
    return chances   
check()
if(won):
    print("you won!")
else:
    print("you lost")
