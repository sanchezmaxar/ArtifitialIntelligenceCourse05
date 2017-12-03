# -*- coding: UTF-8 -*-
from Tkinter import Tk, Label, Button, Entry, StringVar, END, W, E,Text,Menu,Scrollbar
from Unify import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class UnifyCal:

    def __init__(self):

        self.master = Tk()
        self.master.title("GreatUnify")
        self.master.geometry("400x150+400+300")
        self.relleno=Label(self.master,text="\n\t\t")

        self.unificar_button = Button(self.master, text="Unificar", command=lambda:self.unif_y_mod("Unificación",Unify))
        self.modular_button = Button(self.master, text="Modulacion", command=lambda:self.unif_y_mod("Modulación",Modulation))
        self.resolular_button = Button(self.master, text="Resolución", command=lambda:self.unif_y_mod("Resolución",Resolution))
        self.reduc_button = Button(self.master, text="Reducción al absurdo", command=lambda:self.reduc("Reduccción al absurdo",Reduccion_Absurdo))
        self.cerrar_button = Button(self.master, text="Cerrar", command=self.master.destroy)
        self.unificar_button.grid(row=0, column=1, sticky=W+E)
        self.modular_button.grid(row=1, column=1, sticky=W+E)
        self.resolular_button.grid(row=2, column=1, sticky=W+E)
        self.reduc_button.grid(row=3, column=1, sticky=W+E)
        self.cerrar_button.grid(row=4, column=1, sticky=W+E)
        self.relleno.grid(row=0,column=0,sticky=W+E)
        self.relleno.grid(row=1,column=0,sticky=W+E)
        self.relleno.grid(row=2,column=0,sticky=W+E)
        self.relleno.grid(row=3,column=0,sticky=W+E)
        self.relleno.grid(row=4,column=0,sticky=W+E)

    def unif_y_mod(self,cadena,funcion):
        self.master.destroy()
        self.unif=Tk()
        self.unif.title(cadena)
        self.unif.geometry("400x150+400+300")
        self.exp1 = StringVar()
        self.exp2 = StringVar()
        self.salida=StringVar()
        self.salida_label = Label(self.unif, textvariable=self.salida)

        self.label = Label(self.unif, text="Introduce la expresion:")
        self.label1 = Label(self.unif, text="Expresión 1")
        self.label2= Label(self.unif, text="Expresión 2")
        self.label3 = Label(self.unif, text="Salida de "+cadena)

        self.entry = Entry(self.unif,textvariable=self.exp1)
        self.entry2 = Entry(self.unif,textvariable=self.exp2)

        self.close_button = Button(self.unif, text="Regresar", command=lambda:self.regresar(self.unif))
        self.ejecutar_button = Button(self.unif, text=cadena, command=lambda:self.ejecutar(funcion))
        self.or_button1 = Button(self.unif, text="⊻", command=lambda:self.agrOr(self.exp1))
        self.or_button2 = Button(self.unif, text="⊻", command=lambda:self.agrOr(self.exp2))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.label1.grid(row=1, column=0, sticky=W)
        self.label2.grid(row=2, column=0, sticky=W)
        self.label3.grid(row=3, column=0, sticky=W)
        self.salida_label.grid(row=3, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=1, columnspan=3, sticky=W+E)
        self.entry2.grid(row=2, column=1, columnspan=3, sticky=W+E)

        self.close_button.grid(row=5, column=1, sticky=W+E)
        self.ejecutar_button.grid(row=5, column=0, sticky=W+E)
        self.or_button1.grid(row=1, column=4, sticky=W+E)
        self.or_button2.grid(row=2, column=4, sticky=W+E)
    def reduc(self,cadena,funcion):

        self.master.destroy()
        self.reduct=Tk()
        self.reduct.title(cadena)
        self.reduct.geometry("550x350+400+300")
        self.exp1 = StringVar()
        self.exp2 = StringVar()
        self.salida=StringVar()
        self.salida_label = Label(self.reduct, textvariable=self.salida)

        self.label = Label(self.reduct, text="Introduce la expresion:")
        self.label1 = Label(self.reduct, text="Expresión 1")
        self.label2= Label(self.reduct, text="Expresión 2")
        self.label3 = Label(self.reduct, text="Salida de "+cadena)
        self.relleno = Label(self.reduct,text="\t\t")

        self.scroll=Scrollbar(self.reduct)
        self.text = Text(self.reduct, width=40, height=12,yscrollcommand=self.scroll.set)
        self.entry2 = Entry(self.reduct,textvariable=self.exp2)

        self.close_button = Button(self.reduct, text="Regresar", command=lambda:self.regresar(self.reduct))
        self.ejecutar_button = Button(self.reduct, text=cadena, command=lambda:self.ejecutar(funcion,True))
        self.or_button1 = Button(self.reduct, text="⊻", command=lambda:self.agrOr(self.text))
        self.or_button2 = Button(self.reduct, text="⊻", command=lambda:self.agrOr(self.exp2))

        # LAYOUT

        self.relleno.grid(row=0,column=0,sticky=W)
        self.label.grid(row=0, column=1, sticky=W)
        self.relleno.grid(row=1,column=0,sticky=W)
        self.label1.grid(row=2, column=0, sticky=W)
        self.relleno.grid(row=3,column=0,sticky=W)
        self.label2.grid(row=4, column=0, sticky=W)
        self.label3.grid(row=5, column=0, sticky=W)
        self.salida_label.grid(row=5, column=1, columnspan=2, sticky=E)

        self.text.grid(row=2,column=1,columnspan=3,sticky=W+E)
        self.entry2.grid(row=4, column=1, columnspan=3, sticky=W+E)

        self.close_button.grid(row=7, column=1, sticky=W+E)
        self.ejecutar_button.grid(row=7, column=0, sticky=W+E)
        self.or_button1.grid(row=2, column=4, sticky=W+E)
        self.or_button2.grid(row=4, column=4, sticky=W+E)



    def agrOr(self,variable):
        try:
            variable.set(variable.get()+"⊻")
        except:
            variable.insert(END,"⊻")

    def ejecutar(self,funcion,boleano=False):
        if boleano:
            print self.text.get(1.0,END)
            aux=self.text.get(1.0,END).split("\n")
            aux2=[]
            try:
                for i in range(len(aux)):
                    if aux[i]=='':
                        aux.pop(i)
                    else:
                        aux2.append(str(aux.pop(i)))
            except:
                pass
            res=funcion(aux2,str(self.exp2.get()))

        elif funcion==Unify:
            res= funcion(str(self.exp1.get()),str(self.exp2.get()),{})
        else:
            res= funcion(str(self.exp1.get()),str(self.exp2.get()))
        print res
        try:
            if res=="fail" or res=="No se sabe" or res=="Comprobado":
                self.salida.set(res)
            else:
                self.salida.set(res[0])
        except:
            self.salida.set(res)

    def regresar(self,ventana):
        ventana.destroy()
        self.__init__()
my_gui = UnifyCal()
my_gui.master.mainloop()
