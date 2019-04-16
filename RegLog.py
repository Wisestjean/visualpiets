from tkinter import *
def Rejis_Kli():
    #Pran enfomasyon kliyan voye a
    nomKliyan_enfo = NomKliyan.get()
    pasKliyan_enfo = PassKliyan.get()
    #kreye documan ki pou gade enfomasyon kliyan
    dok = open(nomKliyan_enfo+".txt", "w")
    dok.write("Je m'appelle "+nomKliyan_enfo+"\n")
    dok.write("Mon code: "+pasKliyan_enfo)
    dok.close()
    #*****************************************
    #netwaye fom nan le kliyan fini anrejistre
    NMkliyan.delete(0,END)
    pskliyan.delete(0,END)

    Label(fenet_reg,text='Ou Anrejistre ak sikse',bg='sky blue').pack()

def Rejis():
    global fenet_reg
    fenet_reg=Toplevel(kliyan)
    fenet_reg.title('ANREJISTRE KLIYAN 1.0')
    fenet_reg.geometry("300x250")
    fenet_reg.configure(background='cadet blue')
    global NomKliyan
    global PassKliyan
    global NMkliyan
    global pskliyan
    NomKliyan=StringVar()
    PassKliyan=StringVar()
    
    Label(fenet_reg,text='Antre Enfomasyon Paw',bg='sky blue',width="300",height="1",font=("verdana",9)).pack()
    Label(fenet_reg,text=' NomKliyan* ',bg='Cadet Blue',font=("verdana",15)).pack()
    NMkliyan=Entry(fenet_reg,textvariable=NomKliyan)
    NMkliyan.pack()
    Label(fenet_reg,text="",bg='Cadet Blue').pack()
    Label(fenet_reg,text=' PasKliyan* ',bg='Cadet Blue',font=("verdana",15)).pack()
    pskliyan=Entry(fenet_reg,textvariable=PassKliyan,show="*")
    pskliyan.pack()
    Label(fenet_reg,text="",bg='cadet blue').pack()
    Button(fenet_reg,text="ANREJISTRE",height="1",bg='Cadet Blue',width="20",font=("verdana",10),command=Rejis_Kli).pack()
def aksede():
    print("Mpra antre!")

def Fenet_P():
    global kliyan
    kliyan=Tk()
    kliyan.geometry("300x250")
    kliyan.title("Rejis Kliyan 1.0")
    kliyan.configure(background='Cadet Blue')
    Label(text='ENREJISTRE E AKSEDE',bg='sky blue',width="300",height="2",font=("verdana",15)).pack()
    Label(text="",bg='Cadet Blue').pack()
    Button(text="AKSEDE",height="2",bg='Cadet Blue',fg='sky blue',width="30",font=("verdana",10),command=aksede).pack()
    Label(text="",bg='Cadet Blue').pack()
    Button(text="ANREJISTRE",height="2",bg='Cadet Blue',width="30",font=("verdana",10),command=Rejis).pack()

    kliyan.mainloop()

Fenet_P()
