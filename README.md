# QA LLM Evaluation Framework

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

Nesta sprint, foram implementadas regras determinísticas para avaliar respostas geradas por LLMs.

### Validações implementadas

- Verificação de resposta não vazia;
- rejeição de respostas contendo apenas espaços;
- validação de tamanho mínimo;
- rejeição de respostas abaixo do tamanho esperado.

### Testes automatizados

Foram adicionados 6 testes unitários para a classe `ResponseEvaluator`.

Resultado da execução completa:

```text
13 passed

## Estrutura inicial

```text
qa-llm-evaluation-framework/
├── data/
├── prompts/
├── src/
│   └── response_validator.py
├── tests/
│   └── test_response_validator.py
├── .gitignore
├── README.md
└── requirements.txt

