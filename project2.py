class Node:
    def __init__(self,data):
        self.data=data
        self.child_list=[]
        for i in range(26):
            self.child_list.append(None)
        self.End=False    
    def display(self):
        print(self.data,end=" ")
class Dictionary:
    def __init__(self):
        self.root=Node("root")
    def finding_index(self,alphabet):
        if alphabet=="a":
            return 0
        elif alphabet=="b":        
            return 1
        elif alphabet=="c":
            return 2
        elif alphabet=="d":
            return 3
        elif alphabet=="e":
            return 4
        elif alphabet=="f":
            return 5
        elif alphabet=="g":
            return 6
        elif alphabet=="h":
            return 7
        elif alphabet=="i":
            return 8
        elif alphabet=="j":
            return 9
        elif alphabet=="k":
            return 10
        elif alphabet=="l":
            return 11
        elif alphabet=="m":
            return 12
        elif alphabet=="n":
            return 13
        elif alphabet=="o":
            return 14
        elif alphabet=="p":
            return 15 
        elif alphabet=="q":
            return 16
        elif alphabet=="r":
            return 17
        elif alphabet=="s":
            return 18
        elif alphabet=="t":
            return 19
        elif alphabet=="u":
            return 20
        elif alphabet=="v":
            return 21
        elif alphabet=="w":
            return 22
        elif alphabet=="x":
            return 23
        elif alphabet=="y":
            return 24
        elif alphabet=="z":
            return 25
    def insert(self,word):    
        var=self.root
        for i in range(len(word)):
            index=self.finding_index(word[i])
            if var.child_list[index] is None:
                var.child_list[index]=Node(word[i])
            var=var.child_list[index] 
        var.End=True
    def search(self,key):
        var=self.root
        for i in range(len(key)):
            index=self.finding_index(key[i])
            if var.child_list[index] is None:
                return False
            var=var.child_list[index] 
        return True 
    def predication(self,character):
        desire_index=self.finding_index(character)
        intial_list1=[]
        intial_list2=[]
        if self.root.child_list[desire_index] is None:
            return False    
        else:
            variable=self.root.child_list[desire_index]
            intial_list1.append(variable.data)
            while variable.End!=True:
                a=0
                while variable.child_list[a]==None:
                    a+=1
                intial_list1.append(variable.child_list[a].data)
                variable=variable.child_list[a] 
             
            join=''.join(intial_list1)
            intial_list2.append(join)
            return intial_list2     
T1=Dictionary()
print("MENU")
print("To Add word press:a")
print("To Search press:b")
print("To Exit press:x")
print("-----------------")
while True:
    choice=input("Enter choice:")
    if choice=="a":
        word=input("Enter the Word:")
        T1.insert(word)
        print("Inserted...")
        continue
    elif choice=="b":
        key=input("Enter the word to search:")
        print(T1.search(key))
        continue
    elif choice=="x":
        break

#print(T1.predication("s"))

import tkinter as tk
from tkinter import ttk


word_list = []

def key_handler(event=None):
    if event:
            return word_list.append(T1.predication(event.keysym))

def changeMonth():
    comboExample["values"] = word_list

r = tk.Tk()
t = tk.Entry(r)

r.geometry('300x200')
labelone = tk.Label(r,text = "Enter your text")
labelTwo = tk.Label(r,text = "Predicted Words")

comboExample = ttk.Combobox(r, 
                            values=word_list,
                            postcommand=changeMonth)

labelone.grid(row=0,column=0)
t.grid(row=0,column=1)
comboExample.grid(row=1,column=1)
labelTwo.grid(row=1,column=0)

r.bind('<Key>', key_handler)

r.mainloop()
