#link dessa video aula - https://www.youtube.com/watch?v=0o4VtdMhQN4

fruta = 'limao'

print('Suco de %s é o meu favorito!\n' %fruta) #usando string

print('Suco de {} é o meu favorito!\n' .format(fruta)) #usando o comando format

print(f'Suco de {fruta} é o meu favorito!\n') #usando o comando format


cor1 = 'azul' #indice 0
cor2 = 'rosa' #indice 1

print('O ceu é {}, a flor é {}, e o mar é {}.\n'.format(cor1,cor2,cor1)) #impressao com referencia no format.

print('O ceu é {0}, a flor é {1}, e o mar é {0}.\n'.format(cor1,cor2)) #impressao com referencia nos indices.

print(f'O ceu é {cor1}, a flor é {cor2}, e o mar é {cor1}.\n')


conta = 17/3
print('O resultado dessa conta é: %i \n' %conta) # tipo inteiro (%i)

print('O resultado dessa conta é %f \n' %conta) # tipo float (%f)

print('O resultado dessa conta é: {} \n'.format(conta)) #comando format

print(f'O resultado dessa conta é {conta} \n') # comando format sem aproximação decimal

print(f'O resultado dessa conta é {conta:.2f} \n') #comando format, idem acima com aproximacao decimal