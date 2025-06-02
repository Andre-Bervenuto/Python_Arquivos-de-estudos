def multiplicador (numero):
    a = 2 #ESTA VARIAVEL TEM ESCOPO LOCAL
    print(f"Dentro da funcao, a variavel 'a' vale: {a}")
    return a * numero


a = 3 #ESTA VARIAVEL TEM ESCOPO GLOBAL
b = multiplicador (5)
print(f"Fora da funcao, a variavel 'a' vale: {a}\n")

#As linhas 2, 3 e 4 compoem o bloco interno a funcao chamada MULTIPLICADOR().
#Embora as variaveis das linhas 2 e 7 tenham o mesmo nome, elas sao abstraçoes
#a enderecos de memoria diferentes. Dentro da funcao MULTIPLICADOR(), a chamada
#ao nome "a" recupera o valor 2. Fora da funcao MULTIPLICADOR a chamada ao
#nome "a" recupera o valor 3.




# OBSERVE O QUE ACONTECE QUANDO RETIRAMOS A INICIALIZACAO DA VARIAVEL A DENTRO
#DA FUNCAO....

def multiplicador (numero):
    return a * numero

a = 3 #Esta variavel tem escopo global
b = multiplicador (5)
print(f"A variavel 'b' vale: {b}")

#Na linha 27, ao chamar a funcao MULTIPLICADOR(), a variavel "a" será procurada.
#Como nao existe uma variavel "a" no bloco interno, ela é procurada como variavel
#global. Uma vez encontrada o valor recuperado é 3.
