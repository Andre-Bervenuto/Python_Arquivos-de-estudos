numerador = eval(input("Digite o numerador da fracao: "))

denominador = eval(input("\nDigite o denominador da fracao: "))

try: #retorna o print abaixo caso nao ocorra nenhum erro na execução.
    print(f"\nO resultado da divisao foi: {numerador/denominador}")

except ZeroDivisionError: #retorna essa exceção caso seja feita divisao por 0.
    print("\nO denominador informado nao pode ser zero.")

except: #para retornar essa exceção apague a funcao "eval" da linha 3.
    print("\nOs paramentros informados sao invalidos.")

finally: #esta linha aparece independente do resultado do try/except
    print("\nFim do try/except.")
    

