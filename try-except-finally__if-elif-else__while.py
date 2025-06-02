'''Lembrando que se a linha 6 estiver fora do bloco "try/except" o erro
não é tratado na exceção.
Recorte a linha 6, cole antes do "try" e digite letras no teste para ver.'''

try:
    continuar = eval(input('Digite zero pra sair ou outro numero pra continuar: '))

    if continuar >= 1:
        while continuar >= 1:
            x = eval(input('Digite um valor: '))
            y = eval(input('Digite um valor: '))
            soma = x + y
            print('Resultado da soma: ', soma)
            continuar = eval(input("Digite 0 para sair ou "
                                   "outro numero positivo para continuar..."))

    elif continuar == 0:
        print('Voce digitou zero e saiu do programa.\n')

    else:
        print("Valor menor que zero.\n")

except SyntaxError as erro:
    print("Digite algo.\nErro relatado: ",erro,"\n")

except NameError as erro:
    print("Digite numeros. \nErro relatado: ",erro,'\n')

finally:
    print("Fim do programa")

