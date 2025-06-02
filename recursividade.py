#link da video aula https://www.youtube.com/watch?v=fbj5Y19x0fs

#EXEMPLO DE RECURSIVIDADE - CALCULANDO FATORIAL

def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)
x = eval(input('Digite um numero para calcular seu fatorial:'))
resultado = fatorial(x)
print('O fatorial de %f é %f.'%(x,resultado))
print(f'O fatorial de {x:.2f} é {resultado:.2f}')



#EXEMPLO DE RECURSIVIDADE - CALCULANDO FIBONACCI

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
y = eval(input('Digite um numero para calcular seu fibonacci:'))
res = fibonacci(y-1) #esta usando y-1 porque nesse caso esta considerando que comeca a contar a sequencia fibonacci a partir do 0 (zero). Se considerar contagem a partir de 1 remover o (-1).
print(f'Esta contagem esta iniciando a partir do zero, assim o fibonacci da posicao {y} é {res}')


#Outra formula de funcao fibonacci, considerando sequencia a partir do 1 (um). (Formula abaixo da Estacio)
def fibo(n):
    'Esta funcao determina o n-ésimo termo da sequencia fibonacci (Isto é uma docstring)'
    if n == 1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
a = eval(input('Digite um numero para calcular seu fibonacci:'))
valor = fibo(a) #se quiser calcular a partir do zero, colocar: fibo(a-1).
print('O fibonacci da posicao %i é %i.' % (a, valor))
print(help(fibo)) #esta linha executa a docstring da funcao desejada. Nesse caso utilizou "fibo" dentro do utilitario help()