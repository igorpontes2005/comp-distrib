import math
import matplotlib.pyplot as plt

def calcular_disponibilidade(n, k, p):
    
    disponibilidade = 0
    for i in range(k, n + 1):
        comb = math.comb(n, i)
        disponibilidade += comb * (p**i) * ((1-p)**(n-i))
    return disponibilidade


p_plot = 0.90
n_max = 12
servidores = list(range(1, n_max + 1))

leituras = [calcular_disponibilidade(n, 1, p_plot) for n in servidores]
escritas = [calcular_disponibilidade(n, n, p_plot) for n in servidores]
quorums  = [calcular_disponibilidade(n, math.ceil((n+1)/2), p_plot) for n in servidores]

plt.figure(figsize=(10, 6))
plt.plot(servidores, leituras, 'g-o', label='Consulta (k=1) | p=90%')
plt.plot(servidores, quorums,  'b-^', label='Quorum (k≈n/2) | p=90%')
plt.plot(servidores, escritas, 'r-s', label='Atualização (k=n) | p=90%')

plt.title(f'Disponibilidade vs Número de Servidores (p={p_plot*100}%)')
plt.xlabel('Número de Servidores (n)')
plt.ylabel('Disponibilidade do Sistema')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(servidores)
plt.ylim(0, 1.05)

plt.tight_layout()
plt.savefig('grafico_disponibilidade.png')
plt.show()


print("\n" + "="*70)
print(f"{'n':<4} | {'k=1 (p=0.9)':<15} | {'k=1 (p=0.5)':<15} | {'k=n (p=0.9)':<15}")
print("-" * 70)

for n in [1, 3, 5, 10, 15]:
    d1 = calcular_disponibilidade(n, 1, 0.9)
    d2 = calcular_disponibilidade(n, 1, 0.5)
    d3 = calcular_disponibilidade(n, n, 0.9)
    print(f"{n:<4} | {d1:<15.5f} | {d2:<15.5f} | {d3:<15.5f}")
print("="*70)
