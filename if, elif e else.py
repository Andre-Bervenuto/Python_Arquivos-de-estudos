#Python também oferece a estrutura elif, que permite o teste de duas condições de forma sequencial. Essa estrutura
#não existe em C, sendo necessário o encadeamento de estruturas if-else.


idade = eval(input('Informe a idade da criança: '))
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')


#Perceba que a indentação precisa ser ajustada, uma vez que o último else é relativo ao elif. Por isso, eles precisam
#estar alinhados.