#Exemplo de estrutura de decisao, pedindo um numero pro usuario e verificando se o numero é par ou impar.

numero = eval(input("Entre com um numero inteiro positivo:"))

if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")



#Exemplo de estrutura de repeticao...

for num in range (1,21,1):
    if num % 2 == 0:
        print(f"O numero {num} é par.")
    else:
        print(f"O numero {num} é impar.")


#Exemplo de estrutura de repeticao para calculo da media da soma dos numeros pares...
#Obs. A media é a somatoria dos pares, dividido pela quantidade de pares.

soma_par = 0
cont_par = 0

for number in range (1,11,1):
    if number % 2 == 0:
        soma_par = soma_par + number
        cont_par += 1
    else:
        continue #esse continue esta aqui so para explorar mais essa instrucao auxiliar, nesse caso ele vai pular a
                 #iteracao do for

print(f"A soma de numeros pares foi {soma_par}, e a quantidade de numeros foi {cont_par}.")
print(f"A média calculada é {soma_par/cont_par}.")

