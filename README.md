# Algoritmos de Busca e Ordenação em Python

Implementações comentadas de algoritmos clássicos de busca e ordenação, organizadas por categoria e nível de complexidade. Projeto de estudo com foco em entender a lógica de cada algoritmo e suas complexidades de tempo/espaço.

## 🗂️ Estrutura do repositório

```
algoritmos-busca-ordenacao/
├── buscas/
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── jump_search.py
│   ├── interpolation_search.py
│   ├── exponential_search.py
│   ├── fibonacci_search.py
│   └── ternary_search.py
├── ordenacoes/
│   ├── basicas/
│   │   ├── bubble_sort.py
│   │   ├── selection_sort.py
│   │   └── insertion_sort.py
│   ├── eficientes/
│   │   ├── merge_sort.py
│   │   ├── quick_sort.py
│   │   ├── heap_sort.py
│   │   └── shell_sort.py
│   └── nao_comparativas/
│       ├── counting_sort.py
│       ├── radix_sort.py
│       └── bucket_sort.py
├── testes/
│   └── test_algoritmos.py
└── README.md
```

## 📖 Assuntos abordados

### Buscas
| Algoritmo | Complexidade (médio) | Requisito |
|---|---|---|
| Linear Search | O(n) | Nenhum |
| Binary Search | O(log n) | Array ordenado |
| Jump Search | O(√n) | Array ordenado |
| Interpolation Search | O(log log n) | Array ordenado e uniforme |
| Exponential Search | O(log n) | Array ordenado |
| Fibonacci Search | O(log n) | Array ordenado |
| Ternary Search | O(log₃ n) | Array ordenado |

### Ordenações — Básicas
| Algoritmo | Complexidade (médio) | Estável? |
|---|---|---|
| Bubble Sort | O(n²) | Sim |
| Selection Sort | O(n²) | Não |
| Insertion Sort | O(n²) | Sim |

### Ordenações — Eficientes
| Algoritmo | Complexidade (médio) | Estável? |
|---|---|---|
| Merge Sort | O(n log n) | Sim |
| Quick Sort | O(n log n) | Não |
| Heap Sort | O(n log n) | Não |
| Shell Sort | O(n log n) | Não |

### Ordenações — Não-comparativas
| Algoritmo | Complexidade (médio) | Observação |
|---|---|---|
| Counting Sort | O(n + k) | Bom para inteiros em faixa conhecida |
| Radix Sort | O(nk) | Ordena dígito a dígito |
| Bucket Sort | O(n + k) | Bom para dados distribuídos uniformemente |

## 🚀 Como executar

```bash
git clone https://github.com/eduardomendesrocco/Buscas-e-ordenacoes-Searching-and-Sorting.git
cd Buscas-e-ordenacoes-Searching-and-Sorting
python <nome_diretorio>/<nome_arquivo.py>
```

## ✅ Progresso

- [x] Linear Search
- [x] Binary Search
- [x] Jump Search
- [x] Bubble Sort
- [x] Selection Sort
- [x] Insertion Sort
- [ ] Demais algoritmos em andamento

## 🧠 Sobre

Repositório de estudo criado durante o curso técnico, reunindo os principais algoritmos de busca e ordenação implementados em Python.