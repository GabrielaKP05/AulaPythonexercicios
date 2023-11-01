nome_corretor = input("Digite o nome do corretor: ")



quantidade_imoveis_vendidos = int(input("Digite a quantidade de imóveis vendidos: "))



valor_total_vendas = float(input("Digite o valor total das vendas: "))



salario_base = 1500.00



comissao_por_imovel = 200.00


porcentagem_comissao = 0.05



comissao_total = quantidade_imoveis_vendidos * comissao_por_imovel + valor_total_vendas * porcentagem_comissao



salario_final = salario_base + comissao_total

print(f"O salário final do corretor {nome_corretor} é: R$ {salario_final:.2f}")