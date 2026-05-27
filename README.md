## Visão Geral

O **Mission Control AI** é um sistema inteligente de monitoramento de missão espacial desenvolvido em Python com foco em análise operacional, identificação de riscos e automação de decisões.

O projeto simula diferentes ciclos de uma missão espacial experimental, analisando continuamente informações críticas como temperatura, comunicação, bateria, oxigênio e estabilidade operacional.

A partir desses dados, o sistema é capaz de:

- identificar situações de risco;
- classificar automaticamente o estado da missão;
- gerar alertas inteligentes;
- recomendar ações operacionais;
- detectar tendências da missão;
- identificar os sistemas mais afetados;
- gerar relatórios completos no terminal.

O objetivo principal do projeto é aplicar conceitos de pensamento computacional, automação e lógica de programação em um cenário inspirado em centros de controle aeroespaciais.

---

# Contexto da Solução

Missões espaciais dependem de monitoramento constante para garantir segurança, estabilidade e continuidade operacional.

Durante uma missão, diversos sistemas precisam ser analisados simultaneamente:

- controle térmico;
- comunicação com a base;
- gerenciamento energético;
- suporte à vida;
- estabilidade estrutural e operacional.

O Mission Control AI foi projetado para simular esse processo de análise automatizada utilizando regras lógicas desenvolvidas em Python.

---

# Objetivos do Projeto

O sistema foi desenvolvido para:

- armazenar dados simulados de uma missão espacial;

- monitorar múltiplos ciclos operacionais;

- analisar automaticamente os dados coletados;

- calcular pontuações de risco;

- classificar o estado da missão;

- gerar recomendações automáticas;

- identificar tendências de piora ou recuperação;

- detectar a área mais afetada da missão;

- gerar relatórios operacionais detalhados.

---

# Conceitos Aplicados

O projeto utiliza diversos conceitos fundamentais de programação e pensamento computacional:

- Variáveis
- Listas
- Matrizes
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Manipulação de dados
- Automação baseada em regras
- Análise lógica de cenários
- Organização modular de código

---

# Estrutura dos Dados

O sistema utiliza uma matriz principal chamada:

```python
dados_missao
```

Cada linha representa um ciclo da missão espacial.

Cada coluna representa uma informação monitorada:

| Posição | Informação |
|---|---|
| 0 | Temperatura |
| 1 | Comunicação |
| 2 | Bateria |
| 3 | Oxigênio |
| 4 | Estabilidade |

Exemplo:

```python
[24, 92, 88, 96, 90]
```

Representa:

- Temperatura: 24°C
- Comunicação: 92%
- Bateria: 88%
- Oxigênio: 96%
- Estabilidade: 90%

---

# Sistema Inteligente de Alertas

Cada sistema monitorado é classificado automaticamente em:

| Status | Significado |
|---|---|
| NORMAL | Operação segura |
| ATENÇÃO | Instabilidade moderada |
| CRÍTICO | Alto risco operacional |

O sistema utiliza regras específicas para cada área monitorada.

---

# Regras de Temperatura

| Condição | Classificação |
|---|---|
| Menor que 18°C | ATENÇÃO |
| 18°C até 30°C | NORMAL |
| 31°C até 35°C | ATENÇÃO |
| Acima de 35°C | CRÍTICO |

---

# Regras de Comunicação

| Condição | Classificação |
|---|---|
| Menor que 30% | CRÍTICO |
| 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

---

# Regras de Bateria

| Condição | Classificação |
|---|---|
| Menor que 20% | CRÍTICO |
| 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

---

# Regras de Oxigênio

| Condição | Classificação |
|---|---|
| Menor que 80% | CRÍTICO |
| 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

---

# Regras de Estabilidade

| Condição | Classificação |
|---|---|
| Menor que 40% | CRÍTICO |
| 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

# Sistema de Pontuação de Risco

Cada status gera uma pontuação automática:

| Status | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

A soma das pontuações determina a classificação operacional de cada ciclo.

---

# Classificação da Missão

| Pontuação Total | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

# Recomendações Automáticas

O sistema possui uma camada de automação responsável por gerar recomendações inteligentes de acordo com os problemas identificados.

Exemplos:

- Verificar controle térmico da missão;
- Restabelecer comunicação com a base;
- Ativar modo de economia de energia;
- Acionar suporte à vida;
- Reduzir operações não essenciais.

---

# Tendência Operacional

O Mission Control AI compara o primeiro e o último ciclo da missão para identificar tendências operacionais:

- melhora;
- piora;
- estabilidade.

Essa análise permite verificar o comportamento geral da missão ao longo da operação.

---

# Área Mais Afetada

O sistema também calcula qual sistema acumulou maior quantidade de risco durante toda a missão.

Isso permite identificar áreas críticas como:

- energia;
- comunicação;
- temperatura;
- oxigênio;
- estabilidade operacional.

---

# Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python 3 | Desenvolvimento principal |
| Visual Studio Code | Ambiente de desenvolvimento |
| Git | Versionamento |
| GitHub | Hospedagem do projeto |

---

# Integrantes

| Enzo Stahal Freitas | RM569001 |
| Matheus Bruno de Lima | RM572944 |

---

# Objetivo Acadêmico

Projeto desenvolvido para a Global Solution 2026.1 da disciplina:

**Pensamento Computacional e Automação com Python — FIAP**

O trabalho tem como objetivo aplicar lógica computacional e automação em um cenário inspirado em operações aeroespaciais reais.

---

# Considerações Finais

O Mission Control AI demonstra como regras lógicas e estruturas computacionais podem ser utilizadas para criar sistemas inteligentes de monitoramento e apoio à decisão.

Mesmo sem utilização de inteligência artificial avançada ou machine learning, o projeto simula de forma eficiente o comportamento de um centro de controle espacial automatizado, reforçando conceitos fundamentais de programação, análise de dados e automação computacional.