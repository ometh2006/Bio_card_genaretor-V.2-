#Created by Ometh Virusara
import tkinter as tk
from tkinter import Text, ttk

window=tk.Tk()
window.title("Biocar genaretor")
window.geometry('600x400')
gret=tk.Label(text="WELCOME TO ALPAHSOFT")
gret.pack()
btn = ttk.Button(window,text='Close',command=window.quit)
btn.pack()
name=tk.StringVar()
birth=tk.StringVar()
scl=tk.StringVar()
mother=tk.StringVar()
father=tk.StringVar()


def create_clicked():

   
    
    text_box = Text(
    window,
    height=12,
    width=40
    )
    msg1='my name is '+name.get()
    msg2=' I was born in '+birth.get()
    msg3=' My school is '+scl.get()
    msg4=' '+mother.get()+' is my Mother'
    msg5=' '+father.get()+' is my Father'
 
    text_box.pack(expand=True)
    text_box.insert('end',msg1)
    text_box.insert('end ',msg2)
    text_box.insert('end ',msg3)
    text_box.insert('end',msg4)
    text_box.insert('end',msg5)
    text_box.config(state='disabled')
   


  






biocard=ttk.Frame(window)
biocard.pack(padx=10, pady=10, fill='x', expand=True)

name_lable=ttk.Label(biocard,text='name')
name_lable.pack(fill='x', expand=True)

name_entry = ttk.Entry(biocard, textvariable=name)
name_entry.pack(fill='x', expand=True)
name_entry.focus()

birth_lable=ttk.Label(biocard,text='Birth')
birth_lable.pack(fill='x', expand=True)

birth_entry = ttk.Entry(biocard, textvariable=birth)
birth_entry.pack(fill='x', expand=True)
birth_entry.focus()

school_lable=ttk.Label(biocard,text='school')
school_lable.pack(fill='x', expand=True)

school_entry = ttk.Entry(biocard, textvariable=scl)
school_entry.pack(fill='x', expand=True)
school_entry.focus()

mother_lable=ttk.Label(biocard,text='Mother')
mother_lable.pack(fill='x', expand=True)

mother_entry = ttk.Entry(biocard, textvariable=mother)
mother_entry.pack(fill='x', expand=True)
mother_entry.focus()

father_lable=ttk.Label(biocard,text='Father')
father_lable.pack(fill='x', expand=True)

father_entry = ttk.Entry(biocard, textvariable=father)
father_entry.pack(fill='x', expand=True)
father_entry.focus()

login_button = ttk.Button(biocard, text="Genarate", command=create_clicked)
login_button.pack(fill='x', expand=True, pady=10)

devlable=ttk.Frame(window)
devlable.pack(padx=10, pady=10, fill='x', expand=True)

Dev_lable=ttk.Label(biocard,text='Copyright © 2023 By AlphaSoft.',background='tomato',foreground='white')

Dev_lable.pack(padx=0, pady=10,  fill='x', expand=True)





window.mainloop()
