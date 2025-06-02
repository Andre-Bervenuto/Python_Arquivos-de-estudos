def calculaDelta(coef1, coef2, coef3):
    #formula da equacao 2o grau = b ^ 2 - 4 . a . c
    global delta
    delta = coef2 * coef2 - 4 * coef1 * coef3

delta = 0

a = eval(input("Entre com o coeficiente 'a' da equacao: "))
b = eval(input("Entre com o coeficiente 'b' da equacao: "))
c = eval(input("Entre com o coeficiente 'c' da equacao: "))

calculaDelta(a, b, c)

print(f"O valor calculado do delta foi {delta}")

#delta>0 : a equacao tem 2 raizes reais
#delta=0 : a equacao tem 1 raiz real
#delta<0 : a equacao nao tem raiz real

if delta > 0:
    print("A equacao tem 2 raizes reais.")
elif delta == 0:
    print("A equacao tem 1 raiz real.")
else:
    print("A equacao nao tem raiz real.")
        
