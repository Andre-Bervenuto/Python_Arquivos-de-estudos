try:
    x = eval(input("Digite um numero qualquer: "))
    print(f"\nO numero digitado foi {x}")
    
except ValueError:
    print("\nEste erro é levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.")

except TypeError:
    print("\nEste erro é levantado quando uma operação da função é aplicada a um objeto do tipo errado.")

except NameError:
    print("\nEste erro é levantado quando se tenta avaliar um identificador (nome) não atribuído.")

except IndexError:
    print("\nEste erro é levantado quando um índice sequencial está fora do intervalo de índices válidos.")

except IOError:
    print("\nEste erro é levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.")

except ZeroDivisionError:
    print("\nEste erro é levantado quando se tenta dividir por 0.")

except OverflowError:
    print("\nEste erro é levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.")

except KeyboardInterrupt:
    print("\nEste erro e levantado quando o usuário pressiona CTRL + C, a combinação de interrupção.")
    
except SyntaxError:

    print("\nSyntaxError: EOF inesperado durante a análise; Para superar esse tipo de erro em nosso arquivo python, precisamos garantir que não deixamos nenhuma parte de nosso código aberta ou que não tenha a sintaxe adequada")
