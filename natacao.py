# Inicializa uma lista para armazenar os nomes dos nadadores

nomes_nadadores = []

# Inicializa uma lista para armazenar os tempos dos nadadores

tempos_nadadores = []

# Lê o nome e o tempo de cada nadador

for i in range(7):
 nome = input("Digite o nome do nadador: ")
 tempo = float(input("Digite o tempo do nadador (em segundos): "))
 nomes_nadadores.append(nome)
 tempos_nadadores.append(tempo)

# Encontra o nadador com o melhor tempo

melhor_tempo = min(tempos_nadadores)
indice_melhor_tempo = tempos_nadadores.index(melhor_tempo)
nome_melhor_tempo = nomes_nadadores[indice_melhor_tempo]

# Encontra o nadador com o pior tempo

pior_tempo = max(tempos_nadadores)
indice_pior_tempo = tempos_nadadores.index(pior_tempo)
nome_pior_tempo = nomes_nadadores[indice_pior_tempo]

# Calcula o tempo médio dos nadadores

tempo_medio = sum(tempos_nadadores) / len(tempos_nadadores)

# Conta a quantidade de atletas com tempo entre 12s e 15s

quantidade_entre_12_e_15 = len([tempo for tempo in tempos_nadadores if 12 <= tempo <= 15])

# Exibe o relatório

print(f"Melhor tempo: {nome_melhor_tempo} - {melhor_tempo} segundos")
print(f"Pior desempenho: {nome_pior_tempo} - {pior_tempo} segundos")
print(f"Tempo médio: {tempo_medio:.2f} segundos")
print(f"Quantidade de atletas com tempo entre 12s e 15s: {quantidade_entre_12_e_15}")