for num in range(1,11):
    if num == 5:
        continue
    else:
        print(num)
print ('Laço encerrado')

#A instrução continue também funciona da mesma maneira em C e em Python. Ela atua sobre as repetições dos laços for e while,
# como a instrução break, mas não interrompe todas as repetições do laço. A instrução continue interrompe apenas a iteração
# corrente, fazendo com que o laço passe para a próxima iteração.
# O exemplo acima imprime todos os números inteiros de 1 até 10, pulando apenas o 5.
