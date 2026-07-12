# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Para que serve o Eco? |
|---------|---------|-----------------------|
| `limites_orcamento.json` | JSON | Para o Eco saber o teto máximo de dinheiro que o usuário permitiu gastar em cada categoria no mês. |
| `transacoes.csv` | CSV | Para o Eco somar as compras atuais e descobrir se o usuário está perto de estourar o orçamento. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não foram realizadas modificações complexas na estrutura dos dados originais. O conjunto de dados mockados (*mock data*) fornecido no repositório base foi mantido integralmente, pois sua estrutura de colunas (`data`, `descricao`, `categoria`, `valor`, `tipo`) já cobre com precisão todas as necessidades do **Eco**. Apenas criamos o arquivo complementar em JSON para simular os limites de cada categoria.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados do arquivo `transacoes.csv` são carregados no início da sessão utilizando a biblioteca `pandas`, enquanto os limites orçamentários são lidos usando a biblioteca nativa `json` do Python:

```python

import pandas as pd
import json
import os

def carregar_resumo_gastos(caminho_csv):
    if not os.path.exists(caminho_csv):
        return f"Erro: O arquivo {caminho_csv} não foi encontrado! Verifique a pasta."
        
    # Lê o arquivo CSV
    df = pd.read_csv(caminho_csv)
    
    # Filtra apenas as saídas (despesas)
    df_gastos = df[df['tipo'] == 'saida']
    
    # Agrupa por categoria e soma
    resumo = df_gastos.groupby('categoria')['valor'].sum()
    
    # Monta a estrutura de texto que o Eco vai ler
    texto_contexto = "=== DADOS DE CONSUMO QUE O ECO VAI ANALISAR ===\n"
    for categoria, total in resumo.items():
        texto_contexto += f"- Categoria {categoria.upper()}: R$ {total:.2f} gastos até agora.\n"
        
    return texto_contexto



# Executa e mostra o resultado na tela do seu terminal
caminho = "data/transacoes.csv"
print(carregar_resumo_gastos(caminho))

```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O resumo de gastos calculado pelo Python é injetado dinamicamente como Contexto dentro do System Prompt (as instruções do modelo) a cada mensagem. Assim, o Eco sempre lê os saldos atualizados e sabe exatamente quando disparar os alertas, sem risco de errar os cálculos.

---
## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
=== CONFIGURAÇÕES DO CLIENTE (JSON) ===
- Nome do Cliente: João Silva
- Saldo em Conta: R$ 5.000,00

=== DADOS DE LIMITES ESTABELECIDOS (JSON) ===
- Limite para Alimentação: R$ 600,00
- Limite para Lazer: R$ 200,00
- Limite para Transporte: R$ 400,00

=== DADOS DE CONSUMO REAL QUE O ECO VAI ANALISAR (CSV) ===
- Categoria ALIMENTACAO: R$ 570.00 gastos até agora.
- Categoria LAZER: R$ 55.90 gastos até agora.
- Categoria MORADIA: R$ 1380.00 gastos até agora.
- Categoria SAUDE: R$ 188.00 gastos até agora.
- Categoria TRANSPORTE: R$ 295.00 gastos até agora.

DIAGNÓSTICO ATUAL DO SISTEMA:
* Olá, João! A sua categoria Alimentação atingiu 95% do limite permitido (Gatilho de Alerta Crítico).
...
```
