import math

import biblioteca_calculadelta #MODULO CRIADO QUE FOI IMPORTADO (OUTRO ARQUIVO).

a = eval(input("Entre com o coeficiente 'a' da equacao: "))
b = eval(input("Entre com o coeficiente 'b' da equacao: "))
c = eval(input("Entre com o coeficiente 'c' da equacao: "))

delta = biblioteca_calculadelta.calculaDelta(a, b, c)

print(f"O valor calculado do delta foi {delta}")

#delta>0 : a equacao tem 2 raizes reais
#delta=0 : a equacao tem 1 raiz real
#delta<0 : a equacao nao tem raiz real
#formula da raiz da equacao : (-b +- raiz_quadrada(delta))/2 . a

if delta > 0:
    print("A equacao tem 2 raizes reais.")
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    print(f"As raizes calculadas foram {raiz1} e {raiz2}.")
elif delta == 0:
    print("A equacao tem 1 raiz real.")
    raiz = (-b + math.sqrt(delta))/2*a
    print(f"A raiz calculada foi {raiz}.")
else:
    print("A equacao nao tem raiz real.")
        
