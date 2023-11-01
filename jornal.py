# Dicionário com os telejornais e seus respectivos apresentadores

telejornais = {
"Bom Dia Nação": ["Zé PINHEIRO", "Ana Carla ARAÚJO"],
"Jornal Brasileiro": ["Bill BONNER", "CARLA VASCONCELOS"]
}

# Solicita ao usuário o sobrenome do apresentador

sobrenome = input("Digite o sobrenome do apresentador: ")

# Inicializa uma variável para verificar se o apresentador foi encontrado

apresentador_encontrado = False

# Verifica se o sobrenome corresponde a algum apresentador na lista de telejornais

for telejornal, apresentadores in telejornais.items():
  for apresentador in apresentadores:
   if sobrenome.upper() in apresentador.upper():
    print(f"O(a) apresentador(a) {apresentador} apresenta o telejornal {telejornal}.")
    apresentador_encontrado = True
   break

# Se o apresentador não foi encontrado, exibe a mensagem de apresentador desconhecido

if not apresentador_encontrado:
    print("Apresentador(a) desconhecido(a).")