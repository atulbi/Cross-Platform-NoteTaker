from tkinter import *
from tkinter import messagebox
from math import *
#
import simplenote
import time

simplenote = simplenote.Simplenote("devdpnshu@gmail.com","asdasdasd")

i=0

list1= simplenote.get_note_list()[0]

for i in range(0,len(list1)) :
    #time.sleep(1)
    print(list1[i]['key'])

#add_note
string = str ;
note= {'content':'string'}
simplenote.add_note(note)



def helloCallBack():
    list.insert(END, str(entry.get()))
    
    
#str(entry.get())m
w = Tk()
w.title("MessageBox")
w.resizable(width=False, height=False)
w.configure(background = "#003c8f")

h = 0
#Main frame 
r=0

frame = Canvas(w,background = "Gray", width =400,height= 450)
frame.grid(row = r,column=0,padx=5, pady=5,columnspan = 2,sticky= N+S+W+E)

r = r+1
#Listbox

list = Listbox(frame,width = 56,height =29,background= "#808080")
list.grid(row =0,sticky= N+E+W+S)


#scrollbar
scrollbar = Scrollbar(frame,background = "#9be7ff")
scrollbar.grid(row = 0,column =1,sticky = N+S+W+E)



entry = Entry(w,width = 51,bg = "#efebe9")
entry.bind("<Return>", helloCallBack)
entry.grid(row = r, column = 0,padx=5, pady=5,sticky = E+W+N+S)


b1 = Button(w, text='Send',command = helloCallBack , bg = "#C0C0C0")
b1.grid(row = r, column = 1,padx=5, pady=5,sticky = E+W+N+S)
list.configure(yscrollcommand = scrollbar.set)

scrollbar.configure(command = list.yview )
w.mainloop()
