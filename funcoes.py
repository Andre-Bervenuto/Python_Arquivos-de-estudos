#Calcular o delta de uma equação do 2o grau - Funcao com variavel local...

def calculaDelta(coef1, coef2, coef3):#como boa pratica de programacao a funcao deve ficar no inicio do codigo.
    #Delta da equação do 2o grau = b^2-4.a.c
    delta = coef2 * coef2 - 4 * coef1 * coef3
    return delta #Obs. esta variavel delta só existe enquanto esta funcao esta sendo executada.
                 # Uma vez que chega no return o valor da variavel delta para a linha 14 e essa variavel passa
                 # a nao existir apos o termino da funcao.

a = eval(input('Entre com o coeficiente A da equação: '))
b = eval(input('Entre com o coeficiente B da equação: '))
c = eval(input('Entre com o coeficiente C da equação: '))

delta = calculaDelta(a, b, c)

print(f'O valor calculado do delta foi: {delta}')

#delta > 0 - equacao tem 2 raizes reais.
#delta = 0 - equacao tem 1 raiz real.
#delta < 0 - equacao nao tem raiz real.

if delta > 0:
    print('A equação tem 2 raizes reais.')
elif delta == 0:
    print('A equação tem 1 raiz real.')
else:
    print('A equação nao tem raiz real.')

#######################################################################################################################
#Calcular o delta de uma equação do 2o grau - Funcao com variavel global...

def calculaDelta(coef1, coef2, coef3):#como boa pratica de programacao a funcao deve ficar no inicio do codigo.
    #Delta da equação do 2o grau = b^2-4.a.c
    global delta
    delta = coef2 * coef2 - 4 * coef1 * coef3
    #nao existe mais return porque esta usando uma variavel global e esta atribuindo valor a esta variavel.

delta = 0

a = eval(input('Entre com o coeficiente A da equação: '))
b = eval(input('Entre com o coeficiente B da equação: '))
c = eval(input('Entre com o coeficiente C da equação: '))

calculaDelta(a, b, c) #aqui nao precisa mais atribuir valor a variavel delta
                      # porque ele ja foi atribuido na funcao, na variavel global
                      #basta somente executar essa funcao calculaDelta que a variavel
                      #global vai receber o valor na sua execução.

print(f'O valor calculado do delta foi: {delta}')

#delta > 0 - equacao tem 2 raizes reais.
#delta = 0 - equacao tem 1 raiz real.
#delta < 0 - equacao nao tem raiz real.

if delta > 0:
    print('A equação tem 2 raizes reais.')
elif delta == 0:
    print('A equação tem 1 raiz real.')
else:
    print('A equação nao tem raiz real.')


#######################################################################################################################
#Outro exemplo de funcao...

def func1(x):
    x = 10 #essa variavel é local
    print(x)


x = 0 #essa variavel é global
print(x)
func1(x)
print(x)

#A variável x da linha 71 é global. Mas, como existe outra variável com o mesmo nome dentro da função func1() –
# na linha 67, apenas dentro da função func1(), x vale 10 –, chamamos essa variável de local. Assim, o print da
# linha 72 recebe o valor da variável global (0). A execução da linha 73 chama a função func1(), que imprime o valor
# de x válido dentro dela (10). Em seguida, a execução do programa sai da função func1() e o print da linha 74 volta
# a enxergar a variável global x, cujo valor é 0.


