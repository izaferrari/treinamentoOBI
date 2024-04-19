quota_mensal = int(input())
num_meses = int(input())

# Inicializando a quantidade de megabytes não utilizados como a quota mensal
megabytes_nao_utilizados = quota_mensal

# Loop para ler a quantidade de megabytes usados em cada mês e atualizar a quantidade de megabytes não utilizados
for _ in range(num_meses):
    megabytes_usados = int(input())
    megabytes_nao_utilizados += (quota_mensal - megabytes_usados)

# Imprimindo a quantidade de megabytes para o próximo mês
print(megabytes_nao_utilizados)
