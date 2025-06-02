#criando uma janela com texto.
from tkinter import *

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.place(x=50, y=100) #indica o posicionamento do texto
janelaPrincipal.mainloop()



#criando uma janela em branco.
from tkinter import *

janelaPrincipal = Tk()

janelaPrincipal.mainloop()
