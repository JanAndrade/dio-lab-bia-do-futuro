# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** 250,00 (baseado no `transacoes.csv`)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Alerta de limite estourado (ou quase)
- **Pergunta: "Estou perto de estourar o limite de transporte?"
- **Resposta esperada: Agente diz que gastou R$ 150,00 de R$ 400,00 e dá dica de economia.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Formulário de Feedback do ECO

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
| :--- | :--- | :---: |
| Assertividade | "O ECO alertou corretamente sobre os limites de gastos?" |  |
| Utilidade | "As dicas de economia do ECO ajudaram a conscientizar você?" |  |
| Tom de Voz | "O tom firme e amigável do assistente foi adequado?" | |
| Coerência | "A linguagem do ECO foi clara e direta (em até 3 parágrafos)?" |  |

**Comentário aberto:** O que você acha que o ECO poderia melhorar no monitoramento dos gastos?



## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Bloqueio de perguntas fora do escopo (recusou responder sobre a previsão do tempo).
- Respostas rápidas, curtas e diretas, respeitando o limite de até 3 parágrafos.
  
**O que pode melhorar:**
- Ajustar as respostas de recomendação de gastos para que ele reforce que o foco dele é apenas o controle do  orçamento atual.

---

