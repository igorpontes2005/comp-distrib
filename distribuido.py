import math
import matplotlib.pyplot as plt

def calcular_disponibilidade(n, k, p):
    """
    Calcula a disponibilidade (A) usando a distribuição binomial.
    n: total de servidores
    k: mínimo necessário
    p: probabilidade de um servidor individual estar ativo
    """
    disponibilidade = 0
    for i in range(k, n + 1):
        
        combinacao = math.comb(n, i)
        disponibilidade += combinacao * (p**i) * ((1-p)**(n-i))
    return disponibilidade


p = 0.90  
n_max = 10
servidores = list(range(1, n_max + 1))


leituras = [calcular_disponibilidade(n, 1, p) for n in servidores]      
escritas = [calcular_disponibilidade(n, n, p) for n in servidores]      
quorums  = [calcular_disponibilidade(n, math.ceil((n+1)/2), p) if n > 1 else p for n in servidores] 


plt.figure(figsize=(10, 6))
plt.plot(servidores, leituras, 'g-o', label='Consulta (k=1)')
plt.plot(servidores, quorums,  'b-^', label='Quorum (k ≈ n/2)')
plt.plot(servidores, escritas, 'r-s', label='Atualização (k=n)')

plt.title(f'Impacto de n na Disponibilidade (p={p*100}%)')
plt.xlabel('Número de Servidores (n)')
plt.ylabel('Disponibilidade do Sistema')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(servidores)


plt.savefig('grafico_disponibilidade.png')
plt.show()


print(f"{'n':<5} | {'Consulta (k=1)':<15} | {'Quorum':<15} | {'Atualização (k=n)':<15}")
print("-" * 60)
for n in [1, 3, 5]:
    q_val = math.ceil((n+1)/2) if n > 1 else 1
    print(f"{n:<5} | {calcular_disponibilidade(n, 1, p):<15.4f} | {calcular_disponibilidade(n, q_val, p):<15.4f} | {calcular_disponibilidade(n, n, p):<15.4f}")