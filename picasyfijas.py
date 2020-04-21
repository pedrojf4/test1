from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


num=0

class mainwindow:
    def __init__(self, master):

        self.master=master
        master.title("PICAS Y FIJAS")
        master.geometry('800x500')

        self.jugarbtn = Button(master, text="JUGAR", command=self.popup, height=4, width=15)
        self.jugarbtn.place(x=400, y=400)
        
        self.btn = Button(master, text="test", command=self.printval)
        self.btn.place(x=400, y=100)
    
    def printval(self):
        print(self.value)
        
    def popup(self):
        self.w=popupwindow(self.master)

    
       



class popupwindow:
    def __init__(self,master):
        self.top=top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.validar)
        self.b.pack()
"""
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        print(self.value)
        num=self.value    """

class process:

    def validar(self):
    # nb='a'

        self.value=self.e.get()
        self.nb=self.value
        #print(type(nb))
        #print(nb.isnumeric())

        if not self.nb.isnumeric():
            messagebox.showwarning("Error", "ingrese un valor valido")
        else:
            self.nb=int(self.value)

            if self.nb < 1000 or self.nb > 10000:    
                messagebox.showwarning("Error", "ingrese un valor 4 digitos")
            else:
                print('ok')    
                
                print(self.value)
                self.d1=int(self.nb/1000)
                self.r1=self.nb%1000
                self.d2=int(self.r1/100)
                self.d3=int((self.r1%100)/10)
                self.d4=int(self.r1%10)
                self.num=[d1,d2,d3,d4]
                
                self.f,self.p=0,0
                for self.i in range(4):
                    for self.j in range(4):
                        if self.num[i]==self.num[j]:
                            #print(i,j)
                            self.f+=1
                
                if self.f!=4:
                    #print('diferentes')
                    messagebox.showwarning("Error", "ingrese digitos diferentes")
                    
                else:
                    self.calcular(num,nb)

    def calcular(self,num,nb):
        self.h=[2,4,5,7]                         #NUMERO A HALLAR
        self.f,self.p,self.i,self.j=0,0,0,0
        for self.i in range(4):
            for self.j in range(4):
                if self.num[i]==self.h[j]:
                    print(i,j)
                    if self.i==self.j:
                        self.f+=1
                    else:
                        self.p+=1
        self.showpf(p,f,nb)


    def showpf(self,p,f,nb):   

        global k

        self.lbl=[0,1,2,3,4,5,6,7,8,9]
        #k=1
        
        if self.f==1:
            print(f,'fija',self.p,'picas')
            messagebox.showinfo("Error", "%d fija %d picas"%(self.f,self.p))
            self.lbl[k]=Label(window, text="%d     %d fija %d picas"%(self.nb,self.f,self.p))
            self.lbl[k].grid(column=2, row=self.k) 
        elif self.p==1:
            print(f,'fijas',self.p,'pica')
            messagebox.showinfo("Error", "%d fijas %d pica"%(self.f,self.p))
            self.lbl[k]=Label(window, text="%d     %d fijas %d pica"%(self.nb,self.f,self.p))
            self.lbl[k].grid(column=2, row=self.k) 
        else:
            print(self.f,'fijas',self.p,'picas')
            messagebox.showinfo("Error","%d fijas %d picas"%(self.f,self.p))
            self.lbl[k]=Label(window, text="%d     %d fijas %d picas"%(self.nb,self.f,self.p))
            self.lbl[k].grid(column=2, row=self.k) 
        self.top.destroy()
        
        if self.f==4:
            messagebox.showinfo("GANASTE", "DESCUBRISTE EL NUMERO\nCONGRATULATIONS!!!")
        print('k=',self.k)
        self.k+=1




    #return value




#jugarbtn = Button(window, text="JUGAR", command=popup, height=4, width=15)
#jugarbtn.place(x=400, y=400)
        
#btn = Button(window, text="test", command=self.printval)
#btn.place(x=400, y=100)






    

root = Tk()
my_gui= mainwindow(root)

root.mainloop()
 












