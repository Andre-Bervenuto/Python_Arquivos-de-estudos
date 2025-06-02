def multiplicador (numero):
    global a #Todas as referencias à variavel "a" sao para a global
    a = 2    #a global será alterado
    print(f"Dentro da funcao, a variavel 'a' vale: {a}")
    return a * numero


a = 3 #Esta variavel tem escopo global
b = multiplicador(5)
print(f"A variavel 'b' vale: {b}")
print(f"Fora da funcao, a variavel 'a' vale: {a}")


#Perceba que, se a variavel "a" é inicializada na funcao MULTIPLICADOR(),
#qualquer chamada a esse nome dentro da funcao resultará na referencia a
#essa variavel local. Mas seria possivel alterar a variavel "a" global com
#uma instrucao dentro da funcao MULTIPLICADOR()?. Sim, utilizando a palavra
#reservada "global".
