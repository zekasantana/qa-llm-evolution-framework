# QA LLM Evolution Framework

Framework de testes automatizados para avaliar qualidade, segurança, confiabilidade e desempenho de aplicações baseadas em Large Language Models (LLMs).

## Objetivo

Construir um projeto prático de QA para LLMs, evoluindo gradualmente com testes funcionais, datasets, regressão de prompts, segurança, métricas e integração contínua.

## Caso de uso inicial

O sistema classificará chamados de suporte em uma das categorias:

- `HARDWARE`
- `SOFTWARE`
- `ACESSO`
- `OUTROS`

## Tecnologias

- Python 3.13
- Pytest
- OpenAI SDK
- Python Dotenv
- Git e GitHub

## Sprint 1 — Avaliação básica de respostas

Nesta sprint, foram implementadas regras determinísticas iniciais para avaliar respostas geradas por LLMs.

### Validações implementadas

- Verificação de resposta não vazia;
- rejeição de respostas contendo apenas espaços;
- validação de tamanho mínimo;
- rejeição de respostas abaixo do tamanho esperado.

### Testes automatizados

Foram adicionados 6 testes unitários para a classe `ResponseEvaluator`.

Resultado da execução completa da Sprint 1:

```text
13 passed
```

## Sprint 2 — Evolução do avaliador

Nesta sprint, o `ResponseEvaluator` foi evoluído com novas regras configuráveis e uma avaliação consolidada da resposta.

### Validações implementadas

- identificação de padrões proibidos;
- comparação de padrões sem diferenciar maiúsculas e minúsculas;
- rejeição de resposta vazia na validação de padrões;
- validação de tamanho máximo configurável;
- rejeição de respostas acima do limite;
- avaliação consolidada de todos os critérios;
- resultado individual de cada validação;
- decisão final por meio do campo `is_valid`.

### Métodos disponíveis

- `is_not_empty()`;
- `has_minimum_length()`;
- `has_maximum_length()`;
- `is_free_of_forbidden_patterns()`;
- `evaluate()`.

### Testes automatizados

Foram adicionados 10 novos testes unitários na Sprint 2:

- 4 testes para padrões proibidos;
- 3 testes para tamanho máximo;
- 3 testes para avaliação consolidada.

Resultado da execução completa:

```text
23 passed
```

## Sprint 3 — Integração inicial com API de LLM

Nesta sprint, foi criada a primeira camada de integração do framework com uma API real de LLM utilizando o SDK oficial da OpenAI e a Responses API.

### Implementações

- criação da classe `LLMClient`;
- carregamento seguro das configurações com `python-dotenv`;
- leitura da chave por meio da variável `OPENAI_API_KEY`;
- configuração do modelo pela variável `OPENAI_MODEL`;
- uso do modelo `gpt-5-mini` como padrão;
- validação de chave de API ausente;
- validação de prompts vazios;
- normalização do prompt e da resposta;
- suporte à injeção de cliente para testes com mocks;
- criação do arquivo `.env.example` sem dados sensíveis.

### Testes automatizados

Foram adicionados 7 casos de teste para validar:

- geração de resposta com cliente mockado;
- modelo e prompt enviados para a API;
- rejeição de prompt vazio;
- rejeição de prompt contendo apenas espaços;
- rejeição de prompt contendo apenas caracteres de controle;
- ausência da variável `OPENAI_API_KEY`;
- utilização do modelo configurado e do modelo padrão.

Os testes utilizam mocks e não realizam chamadas reais à API, evitando consumo de créditos durante a execução da suíte.

### Resultado

```text
30 passed
```

## Sprint 4 — Evolução com datasets

Nesta sprint, foi implementada a avaliação baseada em datasets para permitir a execução de múltiplos cenários de classificação e o cálculo da acurácia das respostas.

### Implementações

- criação de um dataset no formato JSON;
- inclusão de 8 chamados de suporte;
- distribuição dos chamados entre as categorias `HARDWARE`, `SOFTWARE`, `ACESSO` e `OUTROS`;
- criação da função `load_dataset()` para carregamento dos registros;
- validação da estrutura e do conteúdo do dataset;
- criação da função `calculate_accuracy()`;
- comparação entre categorias esperadas e previstas;
- cálculo percentual da acurácia;
- rejeição de listas vazias;
- rejeição de listas com tamanhos diferentes.

### Testes automatizados

Foram adicionados 10 novos testes:

- 5 testes para o carregamento e a validação do dataset;
- 5 testes para o cálculo de acurácia.

Os testes validam:

- retorno do dataset como lista;
- quantidade de registros;
- presença dos campos obrigatórios;
- entradas não vazias;
- utilização exclusiva das categorias permitidas;
- acurácia de 100%;
- acurácia de 50%;
- acurácia de 0%;
- rejeição de dados vazios;
- rejeição de listas com tamanhos diferentes.

### Resultado

```text
40 passed
```

## Executando os testes

Com o ambiente virtual ativado, execute:

```bash
python -m pytest tests -v
```

## Estrutura atual

```text
qa-llm-evolution-framework/
├── data/
│   └── support_tickets.json
├── prompts/
├── src/
│   ├── dataset_evaluator.py
│   ├── dataset_loader.py
│   ├── llm_client.py
│   ├── response_evaluator.py
│   └── response_validator.py
├── tests/
│   ├── test_dataset_evaluator.py
│   ├── test_dataset_loader.py
│   ├── test_llm_client.py
│   ├── test_response_evaluator.py
│   └── test_response_validator.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```