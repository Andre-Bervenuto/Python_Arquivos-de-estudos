#Abaixo programa do tema 3 - modulo 2 - figura 16 - python.
#O codigo abaixo só dara certo caso seja escolhido a opcao "1". Caso seja escolhido
#a opcao "2" sera executada uma funcao (func2) que nao foi chamada logo depois da
#saida do if/else que é a (func1).
#Obs. mude o "s=func1(10)" para "s=func2(10)" e escolha a opcao "2" para ver...

escolha = eval(input("\n(1o bloco) Escolha uma opção de função: 1 ou 2: "))
if escolha == 1:
    def func1(x):
        return x + 1

else:
    def func2(x):
        return x + 2

s=func1(10)
print(s)





#abaixo mesmo codigo de funcao do exercicio acima, mas agora corrigido com o segundo
#bloco de if/else, desta forma o programa "chama" SOMENTE a funcao "def" que foi
#executada logo acima.

escolha = eval(input("\n(2o bloco) Escolha uma opção de função: 1 ou 2: "))
if escolha == 1:
    def func1(x):
        return x + 1

else:
    def func2(x):
        return x + 2

#segundo bloco de if/else...
if escolha == 1:
    s=func1(10)
    print(s)

else:
    y=func2(20)
    print(y)
