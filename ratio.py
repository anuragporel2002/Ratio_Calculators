from tkinter import *

m=Tk()
m.geometry('550x200')
m.title("Ratio Calculator v1.0")
mlabel=Label(m,text='Ratio Calculator', bg='dark gray', font=('consolas', 24, 'bold'))
mlabel.pack(side=TOP)
m.config(background='dark gray')

textin1=StringVar()
textin2=StringVar()
textin3=StringVar()
textin4=StringVar()

def cal(var1,var2,var3,var4):
    sol=0
    if var4=='x':
        var1=float(var1)
        var2=float(var2)
        var3=float(var3)
        sol=(var2*var3)/var1
    elif var3=='x':
        var1=float(var1)
        var2=float(var2)
        var4=float(var4)
        sol=(var1*var4)/var2
    elif var2=='x':
        var1=float(var1)
        var4=float(var4)
        var3=float(var3)
        sol=(var1*var4)/var3
    elif var1=='x':
        var4=float(var4)
        var2=float(var2)
        var3=float(var3)
        sol=(var2*var3)/var4
    return sol

def calbut():
    global textin4,textin3,textin2,textin1
    var1=textin1.get()
    var2=textin2.get()
    var3=textin3.get()
    var4=textin4.get()
    sol=cal(var1,var2,var3,var4)
    if var4=='x':
        textin4.set('x='+str(sol))
    elif var3=='x':
        textin3.set('x='+str(sol))
    elif var2=='x':
        textin2.set('x='+str(sol))
    elif var1=='x':
        textin1.set('x='+str(sol))     


en1=Entry(m,font=("tempus sans itc",18,'bold'),textvar=textin1,width=5,bd=5,bg='powder blue')
en1.place(x=10, y=50)
lab1=Label(m, text=":", bg='dark gray', font=('tempus sans itc',24,'bold'))
lab1.place(x=120, y=50)
en2=Entry(m,font=("tempus sans itc",18,'bold'),textvar=textin2,width=5,bd=5,bg='powder blue')
en2.place(x=150,y=50)
lab2=Label(m, text="::", bg='dark gray', font=('tempus sans itc',24,'bold'))
lab2.place(x=260, y=50)
en3=Entry(m,font=("tempus sans itc",18,'bold'),textvar=textin3,width=5,bd=5,bg='powder blue')
en3.place(x=300,y=50)
lab3=Label(m, text=":", bg='dark gray', font=('tempus sans itc',24,'bold'))
lab3.place(x=410, y=50)
en4=Entry(m,font=("tempus sans itc",18,'bold'),textvar=textin4,width=5,bd=5,bg='powder blue')
en4.place(x=440,y=50)

but1=Button(m, text="Calculate", font=('tempus sans itc',18,'bold'),bd=5,command=calbut)
but1.place(x=190, y=120)
l=Label(m,text="All copyrights Reserved. Developed by Anurag Porel", font=('consolas',8))
l.pack(side=BOTTOM)

if __name__=="__main__":
    m.mainloop()