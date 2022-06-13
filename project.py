class Node:
    def __init__(self,alphabet):
        self.alphabet=alphabet
        self.list=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.markasEnd=False

class Tree:
    def __init__(self):
        self.root= self.node("Root")
    def node(self,character):
        return Node(character)
    
    def index(self, character):
        '''alphabet_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","n",\
            "o","p","q","r","s","t","u","v","w","x","y","z"]
        for alpha in (alphabet_list):
            if character==alpha:
                index=alphabet_list.index(alpha)
                return index
                break'''
        return ord(character)-ord("a")                                                                                                                              

    def insert_word(self,word):
        current=self.root 
        for i in range(len(word)):
            index=self.index(word[i])
            if not current.list[index]:
                current.list[index] = self.node(word[i])
            current = current.list[index]  
        current.markasEnd = True
            
    def search_word(self,word):
        current=self.root
        for i in range(len(word)):
            index=self.index(word[i])
            if not current.list[index]:
                return 'Word not exits'
            current = current.list[index]
        return 'Congrats!...Word Found'
    def suggestion(self,word):
        particular_index=self.index(word)
        word_list1=[]
        word_list2=[]
        if self.root.list[ particular_index]==None:
            print("No word Exists")    
        elif self.root.list[particular_index]!=None:
            current=self.root.list[particular_index]
            word_list1.append(current.alphabet)
            while current.markasEnd!=True:
                count=0
                while current.list[count]==None:
                    count+=1
                word_list1.append(current.list[count].alphabet)
                current=current.list[count] 
             
            join=''.join(word_list1)
            word_list2.append(join)
            return word_list2               
    
    def Display(self):
        print("-----------INSTRUTIONS---------")
        print(" To Insert Word in a Dictionary press:a","\n","TO search a word in a dictionary press:b","\n","To Exit press:x")
        while True:
            insert=input("To insert word press a:").lower()
            if insert=="a":
                word=input("Enter the word:")
                T1.insert_word(word)
                print("Insert Successfully.....")
                continue
            elif insert=="x":
                print("Exit Successfully....")
                break
        while True:
            search=input("To search a word press b:").lower()
            if search=="b":
                element = input("Enter A word: ")
                print(T1.search_word(element))
                continue
            elif search=="x":
                print("Exit Successfully....")
                break
        print("Suggest:")    
        print(T1.suggestion("s"))    

        
                  
T1=Tree()
T1.Display()


import tkinter as tk
from tkinter import ttk


listt = []

def key_handler(event=None):
    if event:
            return listt.append(T1.suggestion(event.keysym))

def changeMonth():
    comboExample["values"] = listt

r = tk.Tk()
t = tk.Entry(r)

r.geometry('300x200')
labelone = tk.Label(r,text = "Enter your text")
labelTwo = tk.Label(r,text = "Predicted Words")

comboExample = ttk.Combobox(r, 
                            values=listt,
                            postcommand=changeMonth)

labelone.grid(row=0,column=0)
t.grid(row=0,column=1)
comboExample.grid(row=1,column=1)
labelTwo.grid(row=1,column=0)

r.bind('<Key>', key_handler)

r.mainloop()