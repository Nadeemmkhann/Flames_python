from tkinter import *

def checkFlames():
    str1 = p1_entry.get()
    str2 = p2_entry.get()
    flames = ['Friends','Love','Affection','Marriage','Enemy','Sibling']
    resultant = ''
    for ch in str1.lower():
        if ch in str2.lower():
            indx1 = str1.lower().index(ch)
            indx2 = str2.lower().index(ch)
            str1 = str1[:indx1] + str1[indx1+1:]
            str2 = str2[:indx2] + str2[indx2+1:]
    resultant = str1 + str2
    while len(flames) != 1:
        index = (len(resultant) % len(flames))-1
        del flames[index]
        if index > 0:
            flames = flames[index:] + flames[:index]
    if len(resultant) > 0:
        msg.config(text = "Relationship : Whoo!! "+flames[0])


root = Tk()

root.title("FLAMES")

root.geometry("500x410")
root.minsize(500,400)
root.config(bg='#fd92a0') 
welcomeLabel = Label(text="Welcome To Flames",bg="#f55469",font="Comi 20 bold",fg="white",borderwidth=3,relief=RIDGE,padx=5,pady=5)
welcomeLabel.pack(pady=5,fill='x',padx=5)

f1 = Frame(root,borderwidth=5,bg="#f55469",relief=RIDGE)
f1.pack(padx=20,pady=20,fill='x')

f2 = Frame(f1,borderwidth=5,bg="#f55469",relief=RIDGE)
f2.pack(padx=20,pady=20,fill='x')
f3 = Frame(f1,borderwidth=5,bg="#f55469",relief=RIDGE)
f3.pack(padx=20,pady=20,fill='x')

person1 = Label(f2,text="Person 1  ",bg="#f55469",font="Comi 15 bold",fg="white")
person1.pack(side=LEFT)
person2 = Label(f3,text="Person 2  ",bg="#f55469",font="Comi 15 bold",fg="white")
person2.pack(side=LEFT)

p1_entry = Entry(f2,textvariable=StringVar())
p1_entry.pack(side=TOP,pady=5)
p2_entry = Entry(f3,textvariable=StringVar())
p2_entry.pack(side=TOP,pady=5)

b1 = Button(f1,text='Check',command=checkFlames,bg="#ff2a46",font="Comi 15 bold",fg="white")
b1.pack(pady=10)

f4 = Frame(f1,borderwidth=5,bg="#f55469",relief=RIDGE)
f4.pack(padx=20,pady=20,fill='x')
msg = Label(f4,text='Relatioship :',bg="#f55469",font="Comi 15 bold",fg="white")
msg.pack(side=LEFT)

root.mainloop()