## Visão Geral  
Este projeto contém soluções para dois desafios técnicos propostos pelo Sicredi, seguindo boas práticas de código limpo, documentação e testes unitários.  
A estrutura do projeto está organizada em `src/` (código principal) e `tests/` (testes unitários).

---

## Questão 1: Identificação de Maiores Devedores  
**Objetivo:**  
Retornar os `N` maiores devedores que ainda não renegociaram seus contratos.

### **Abordagem**  
1. **Filtragem Eficiente:**  
   - Usamos um `set` para verificar contratos renegociados em **O(1)**.  
2. **Ordenação Decrescente:**  
   - Ordenamos os contratos pelo saldo devedor para garantir priorização correta.  
3. **Validação de Entrada:**  
   - Tratamos casos onde `top_n` é maior que a lista filtrada ou ≤ 0.  

### **Exemplo de Uso**  
```python
contracts = [
    Contract(1, 100),
    Contract(2, 200),
    Contract(3, 300)
]
renegotiated = [3]
top_n = 2

result = Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n)
print(result)  # Output: [2, 1]
```

---

## Questão 2: Otimização de Viagens de Carro-Forte  
**Objetivo:**  
Calcular o número mínimo de viagens para atender requisições de agências, combinando no máximo 2 por viagem e respeitando um valor máximo (`n_max`).

### **Abordagem**  
1. **Algoritmo Two Pointers:**  
   - Ordenamos as requisições em ordem decrescente e usamos dois ponteiros para combinar a maior e a menor requisição disponíveis.  
2. **Complexidade O(n log n):**  
   - A ordenação domina a complexidade, garantindo eficiência mesmo para grandes listas.  

### **Exemplo de Uso**  
```python
orders = [70, 30, 10]
n_max = 100

result = Orders().combine_orders(orders, n_max)
print(result)  # Output: 2
```

---

## Como Executar os Testes Unitários  
**Pré-requisitos:**  
- Python 3.8+ instalado.  

**Passo a Passo:**  
1. **Execute os testes:**  
   ```bash
   python -m unittest discover tests
   ```  

---

> **Nota:**  
> O projeto foi desenvolvido com foco em clareza e eficiência, seguindo PEP8, Black e boas práticas de desenvolvimento.  
> A documentação dos métodos inclui exemplos e explicações para facilitar a manutenção futura.