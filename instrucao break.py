for num in range(1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')

#A instrução break funciona da mesma maneira em C e em Python. Ela interrompe as repetições dos laços for e while. Quando
# a execução do programa chega a uma instrução break, a repetição é encerrada e o fluxo do programa segue a partir da
# primeira instrução seguinte ao laço.

#Para exemplificar o uso da instrução break, vamos voltar ao primeiro exemplo do laço while, utilizando o laço infinito.
# O laço será encerrado quando o usuário inserir a palavra ‘sair’

while True:
    palavra = input('Entre com uma palavra: ')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')


#Caso haja vários laços aninhados, o break será relativo ao laço em que estiver inserido.
while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. ')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. ')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')
