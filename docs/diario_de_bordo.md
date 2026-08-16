# Diário de Bordo - TributAI

## 2026-08-13

### Organização do Projeto

- Revisão da estrutura do projeto TributAI.
- Definição da estratégia de processamento dos documentos legais da Reforma Tributária.
- Organização dos diretórios de dados processados.

### Chunking Jurídico

- Implementado o processo de segmentação jurídica dos documentos.
- Definido que cada artigo deve ser tratado como um chunk independente.
- Implementado tratamento específico para anexos.

### Estatísticas

Resultado final da preparação dos documentos:

- 1172 chunks gerados.

---

## 2026-08-14

### Escolha do Modelo de Embeddings

Após análise das opções disponíveis, foi escolhido:

```text
ulysses-camara/legal-bert-pt-br

## 2026-08-15

### ORDS

Primeiro endpoint REST criado:

POST /ords/tributai/v1/documento

Foi identificado que o payload JSON deve ser acessado por:

:body_text

e não por:

:body

A API retornou com sucesso:

{
  "status": "success",
  "id_documento": 36
}

