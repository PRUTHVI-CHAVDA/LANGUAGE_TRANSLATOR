from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk() #for importing graphics
root.title("Translator")
root.geometry("400x790")
# root.config(bg='pink')
bg = PhotoImage(file = "background.png") #for importing background image
label1 = Label( root, image = bg)
label1.pack(fill= "both", expand=True)


lab_txt = Label(root, text="TRANSLATOR", font=("Time New Roman", 30, "bold"),bg='#FFE4C4',fg="black")#.pack()
lab_txt.place(x=48, y=10, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root, text="INPUT TEXT", font=("Time New Roman", 20, "bold"),bg='WHITE',fg="black")
lab_text.place(x=110, y=70, height=25, width=180)

sor_txt = Text(frame, font=("Time New Roman", 13, "bold"), wrap=WORD)
sor_txt.place(x=13, y=110, height=300, width=375)

list_text = list(LANGUAGES.values())
combo_sor = ttk.Combobox(frame, values=list_text)
combo_sor.place(x=14, y=440, height=25, width=110) #change size
combo_sor.set("english")

button_change = Button(frame, text="Translate", font=("Time New Roman", ),relief=RAISED,command=data)
button_change.place(x=150, y=440, height=25, width=100) #change size

combo_dest = ttk.Combobox(frame, values=list_text)
combo_dest.place(x=278, y=440, height=25, width=110) #change size
combo_dest.set("hindi")

lab_txt = Label(root, text="OUTPUT TEXT", font=("Time New Roman", 20, "bold"))
lab_txt.place(x=105, y=480, height=25, width=200) # change width

dest_txt = Text(frame, font=("Time New Roman", 13, "bold"), wrap=WORD)
dest_txt.place(x=13, y=520, height=250, width=375) #change sixze

root.mainloop()