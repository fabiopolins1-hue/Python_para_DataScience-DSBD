#nome, idade, cidade = input(
#    "Digite o nome, idade e cidade separados por espaço: "
#    ).split(",")

#idade = int(idade)
#print(f'{nome} tem {idade} anos e mora em {cidade}')

nomeidadecidade = input("Digite o nome, idade e cidade separados por espaço: ")

print(f'{nomeidadecidade}')

nome, idade, cidade = nomeidadecidade.split()

print(f'{nome} tem {idade} anos e mora em {cidade}')