#Link dessa video aula: https://www.youtube.com/watch?v=uxYfWjBeAZ8

conta = 0 #Iniciando uma variavel qualquer.

try:
    print("Inicio do bloco try")    
    valor1 = eval(input("\nDigite o valor 1: "))
    valor2 = eval(input("\nDigite o valor 2: "))
    print("\nCalculando a conta\n")
    conta = valor1/valor2
    print("Fim do bloco try")
    
except Exception as info_erro: #O "exception" é uma excecao generica(um geralzao). O "info_erro" a partir do momento que surge a excecao; ele cria uma instancia desse "info_erro". A variavel "info_erro" é a variavel de excecao.
    print("O erro encontrado foi:",info_erro)
    
else:      #Vide observacao abaixo do bloco else.
    print("\nInicio do bloco else")
    print(f"\nO resultado da conta é {conta}\n")
    print("Fim do bloco else")

finally:   #Vide observacao abaixo do bloco finally.
    print("\nBloco finally")



#Observações:
    
#EXCEPT - O bloco "except" é executado caso DÊ erro no bloco "try".
    
#O nome "info_erro" pode ser substituido por qualquer outro nome (é uma variavel que ira informar o erro que deu na excecao).

#ELSE - O bloco "else" é executado caso NÃO dê erro no bloco "try".
    
#FINALLY - O bloco finally é executado em qualquer instancia (muito usado para fechar Banco de dados).

#Isto porque o bloco finally é executado com o programa dando erro ou nao (desde que esse erro esteja dentro do try/except).
