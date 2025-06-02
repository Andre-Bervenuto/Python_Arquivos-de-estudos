#Outra formula de funcao fibonacci, considerando sequencia a partir do 1 (um). (Formula abaixo da Estacio)
def fibo(n):
    'Esta funcao determina o n-ésimo termo da sequencia fibonacci (Isto é uma docstring)'
    if n == 1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
a = eval(input('Digite um numero para calcular seu fibonacci:')) #variavel ''a'' para captar o numero escolhido pelo usuario.
valor = fibo(a) #se quiser calcular a partir do zero, colocar: fibo(a-1). Variavel ''valor'' retorna o valor correspondente a variavel ''a'' que foi definida pelo usuario.
print('O fibonacci da posicao %i é %i.' % (a, valor))
print(f'O fibonacci da posicao {a} é {valor}.')
print(help(fibo)) #esta linha executa a docstring da funcao desejada. Nesse caso utilizou "fibo" dentro do utilitario help()