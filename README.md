# comp-distrib
# Computação Distribuída: Disponibilidade em Sistemas Replicados

**Aluno:** Igor Honório de Paiva Pontes  
**Matrícula:** 2315064

**Aluno:** Raul Tiezzi Henriques  
**Matrícula:** 1810521


Este repositório contém a resolução dos exercícios 1.1 e 1.2. O trabalho foca na análise probabilística da disponibilidade de serviços replicados sob diferentes estratégias de consistência.

---

## 📖 Exercício 1.1: Dedução Matemática

O objetivo foi deduzir a fórmula que calcula a disponibilidade de um serviço com $n$ servidores, onde pelo menos $k$ devem estar ativos para que o sistema seja considerado disponível.

### Parâmetros:
- $n$: número total de servidores ($n > 0$).
- $k$: número mínimo de servidores necessários ($0 < k \le n$).
- $p$: probabilidade de um servidor estar disponível ($0 \le p \le 1$).

### Fórmula Geral (Distribuição Binomial)
A disponibilidade $A$ é a soma das probabilidades de termos de $k$ até $n$ servidores ativos:

$$A(n, k, p) = \sum_{i=k}^{n} \binom{n}{i} p^i (1-p)^{n-i}$$

### Casos Extremos:
1.  **Operação de Consulta ($k = 1$):** O serviço está disponível se **pelo menos um** servidor estiver ativo.
    - Fórmula: $A = 1 - (1 - p)^n$
2.  **Operação de Atualização ($k = n$):** O serviço só está disponível se **todos** os servidores estiverem ativos simultaneamente.
    - Fórmula: $A = p^n$

---

## 📊 Exercício 1.2: Cálculo Analítico e Simulação

Foi implementado um script em Python para validar as fórmulas e visualizar o comportamento do sistema conforme o número de réplicas aumenta.

### Tabela de Disponibilidade (Exemplo com $p = 0.90$)

| Servidores ($n$) | Consulta ($k=1$) | Quorum ($k = \lceil n/2 \rceil$) | Atualização ($k=n$) |
| :--- | :--- | :--- | :--- |
| 1 | 90,00% | 90,00% | 90,00% |
| 3 | 99,90% | 97,20% | 72,90% |
| 5 | 99,99% | 99,14% | 59,04% |

### Análise dos Resultados
- **Escalabilidade Positiva ($k=1$):** Adicionar servidores melhora drasticamente a disponibilidade para leituras.
- **Escalabilidade Negativa ($k=n$):** Adicionar servidores para escritas estritas (consistência forte absoluta) prejudica a disponibilidade do sistema.
- **Estratégia de Quorum:** Apresenta o melhor equilíbrio entre disponibilidade e tolerância a falhas.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a simulação e gerar os gráficos em sua máquina local.

### 1. Pré-requisitos
Você precisará do **Python 3.x** instalado. Além disso, o script utiliza a biblioteca `matplotlib` para a geração dos gráficos.

### 2. Instalação de Dependências
Abra o seu terminal e instale a biblioteca necessária via pip:
```bash
pip install matplotlib


