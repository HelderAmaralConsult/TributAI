# Arquitetura do TributAI

## Objetivo

Criar um agente RAG especializado na Reforma Tributária Brasileira.

---

## Fontes de Conhecimento

### Emenda Constitucional

- EC 132/2023

### Leis Complementares

- LC 214/2025
- LC 215/2025
- LC 216/2025
- LC 227/2026

---

## Pipeline

```text
PDF
 ↓
Extração de Texto
 ↓
TXT
 ↓
Chunking Jurídico
 ↓
Embeddings
 ↓
Oracle Vector Search
 ↓
Gemini
 ↓
Resposta
```

---

## Estrutura Atual

```text
data/

raw/
processed/
chunks/
embeddings/
```

---

## Estratégia de Chunking

Cada artigo é transformado em um chunk independente.

Exemplo:

```json
{
  "documento": "Lei_Complementar_214",
  "artigo": "Art. 14",
  "conteudo": "..."
}
```

---

## Tratamento de Anexos

Anexos são tratados como chunks independentes.

Exemplo:

```text
ANEXO I
ANEXO II
ANEXO III
```

---

## Front-end

Oracle APEX 26.1

---

## Banco de Dados

Oracle Database 26ai

Estratégia planejada:

```sql
VECTOR(768)
```

para armazenamento dos embeddings jurídicos.

---

## Modelo LLM Planejado

Google Gemini

Utilizado na camada de geração de respostas.
