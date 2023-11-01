# Inicializa uma lista para armazenar os nomes dos medicamentos

nomes_medicamentos = []

# Inicializa uma lista para armazenar os preços dos medicamentos

precos_medicamentos = []

# Recebe o nome e o preço de 5 medicamentos

for i in range(5):
 nome = input("Digite o nome do medicamento: ")
nomes_medicamentos.append(nome)


for i in range(5):
 preco = float(input("Digite o preço do medicamento (em R$): "))
precos_medicamentos.append(preco)

# Encontra o medicamento mais barato

indice_medicamento_mais_barato = precos_medicamentos.index(min(precos_medicamentos))
medicamento_mais_barato = nomes_medicamentos[indice_medicamento_mais_barato]
preco_mais_barato = precos_medicamentos[indice_medicamento_mais_barato]

# Calcula a média aritmética dos preços dos medicamentos

media_precos = sum(precos_medicamentos) / len(precos_medicamentos)


# Exibe o nome e o preço do medicamento mais barato

print(f"O medicamento mais barato é '{medicamento_mais_barato}' com o preço de R$ {preco_mais_barato:.2f}")

# Exibe a média aritmética dos preços dos medicamentos

print(f"A média dos preços dos medicamentos é: R$ {media_precos:.2f}")