from tkinter import *
from tkinter import messagebox

top = Tk()
top.configure(background="gray")
top.title("Todo")
top.geometry("400x500")
L1 = Label(top, text="Task")
L1.pack(side = LEFT)

E1 = Entry(top, bd = 5 ,width = 100)

E1.pack(side = RIGHT)
Todos = []


def already():
   messagebox.showinfo("Its here", " its already here !! , this task is already in todo list")
def addMenuItems():


    itemToAdd = E1.get()
    if itemToAdd in Todos :
        already()

    else:
        Todos.append(itemToAdd)
        i = 0
        print("this is the items of todo ")
        for x in Todos:
            print(i + 1, ".", Todos[i])
            i += 1
        E1.delete(0, END)


def clearAll():
    Todos.clear()
    E1.delete(0,END)
def showAll ():
            iu = 1
            str = Todos
            sh = Tk()
            sh.geometry("400x400")
            sh.title("show time !")
            lb = Listbox(sh)
            lb.place(x = 0 , y= 0)
            for x in Todos :
                print(x)

                lb.insert(iu ,  x)
                iu = iu +1


            messagebox.showinfo("Its here",
                                str

                                )




B = Button(top , text="insert" , command = addMenuItems)
clear =Button(top ,text ="clear all" ,command = clearAll)
clear.place(x =250 ,y=  270)


B.place(x = 200 , y= 270)
show = Button(top , text = "Show" , command = showAll)
show.place(x = 310 , y =270)
B.pack
def displayAll():
    text = Text(top)

    text.place(x=150 , y = 350 )
    # results = Tk()
    # results.geometry("300x300")
    # text = Text(results )
    # text.insert(INSERT , Todos)
    # results.mainloop()


top.mainloop()

