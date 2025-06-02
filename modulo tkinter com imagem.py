from tkinter import *

def funClicar():
    print("Botao pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="palmeiras.gif")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = "Clique", command = funClicar)
botao.pack()

janelaPrincipal.mainloop()
