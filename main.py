
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
chances=0
count=0
def check():
    while(chances<6):
       userinput = input("guess a character")
       count=0
       for x in range(0,len(pickword())):
          if(pickword()[x]==userinput):
              guessed[x]=userinput
              break
          else:
              count+=1
       if(count==len(pickword())):
           chances+=1
        
        
