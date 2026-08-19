# TributAI

Assistente inteligente baseado em IA para consulta da Reforma Tributária Brasileira utilizando busca semântica, embeddings jurídicos e Oracle AI Vector Search.

## Sobre o Projeto

O TributAI é uma solução de Inteligência Artificial desenvolvida para facilitar a consulta e compreensão da legislação relacionada à Reforma Tributária Brasileira.

O projeto utiliza documentos oficiais públicos, como:

- Emenda Constitucional nº 132/2023
- Lei Complementar nº 214/2025
- Regulamentações complementares
- Notas Técnicas
- Guias Oficiais
- Publicações da Receita Federal

A solução permite que usuários realizem perguntas em linguagem natural e recuperem os trechos mais relevantes da legislação utilizando busca semântica baseada em embeddings.

---

## Objetivo

Reduzir o tempo gasto na pesquisa e interpretação da legislação tributária, oferecendo uma experiência de consulta simples, rápida e baseada em fontes oficiais e auditáveis.

---

## Situação Atual

✅ MVP funcional concluído.

Atualmente o TributAI já é capaz de:

- Receber perguntas em linguagem natural
- Gerar embeddings utilizando Legal-BERT
- Executar busca semântica utilizando Oracle AI Vector Search
- Recuperar os 5 trechos mais relevantes da legislação
- Exibir os resultados através do Oracle APEX
- Registrar histórico das consultas realizadas
- Disponibilizar serviços REST protegidos por HTTPS

---

## Arquitetura Atual

```text
Usuário
   │
   ▼
Oracle APEX
   │
   ▼
REST Data Source
   │
   ▼
HTTPS
   │
   ▼
tributai.duckdns.org
   │
   ▼
Nginx (Reverse Proxy)
   │
   ▼
Gunicorn
   │
   ▼
Flask
   │
   ▼
Legal-BERT (ulysses-camara/legal-bert-pt-br)
   │
   ▼
Geração de Embeddings
   │
   ▼
Oracle AI Vector Search
   │
   ▼
Busca Semântica nos Chunks da Legislação
   │
   ▼
Top 5 Resultados Mais Relevantes
```

---

## Fluxo Implementado

```text
Pergunta em Linguagem Natural
   │
   ▼
Geração de Embedding
   │
   ▼
Oracle AI Vector Search
   │
   ▼
VECTOR_DISTANCE
   │
   ▼
Top 5 Chunks Mais Relevantes
   │
   ▼
Exibição no Oracle APEX
   │
   ▼
Registro do Histórico da Consulta
```

---

## Tecnologias Utilizadas

### Front-end

- Oracle APEX

### Backend

- Python
- Flask
- Gunicorn
- Nginx
- systemd

### Inteligência Artificial

- Legal-BERT PT-BR (`ulysses-camara/legal-bert-pt-br`)
- Sentence Transformers

### Banco de Dados

- Oracle Autonomous Database 23ai
- Oracle AI Vector Search
- Oracle VECTOR
- Oracle VECTOR_DISTANCE

### Infraestrutura

- Oracle Cloud Infrastructure (OCI)
- DuckDNS
- Let's Encrypt

### DevOps e Versionamento

- Git
- GitHub

---

## Endpoints da API

### Verificação de Saúde

Endpoint utilizado para monitoramento da aplicação.

```http
GET /health
```

Exemplo:

```http
GET https://tributai.duckdns.org/health
```

Resposta:

```json
{
  "status": "ok"
}
```

---

### Geração de Embeddings

Endpoint responsável pela geração dos embeddings utilizados na busca semântica.

```http
POST /embed
```

Exemplo:

```http
POST https://tributai.duckdns.org/embed
Content-Type: application/json
```

Body:

```json
{
  "pergunta": "Qual a alíquota do Imposto Seletivo para alimentos?"
}
```

Resposta:

```json
{
  "embedding": [
    -0.0604,
    -0.0450,
    -0.0210
  ]
}
```

---

## Funcionalidades Implementadas

- Consulta em linguagem natural
- Busca semântica sobre legislação tributária
- Geração de embeddings jurídicos
- Busca vetorial utilizando Oracle AI Vector Search
- Recuperação dos 5 trechos mais relevantes
- Histórico de consultas
- API REST para geração de embeddings
- Implantação em Oracle Cloud Infrastructure (OCI)
- Publicação segura via HTTPS

---

## Estrutura do Projeto

```text
TributAI/
│
├── apex/
│   └── Export da aplicação Oracle APEX
│
├── db/
│   ├── ddl/
│   ├── repositories/
│   └── scripts/
│
├── docs/
│   ├── diario_de_bordo.md
│   └── documentacao_tecnica.md
│
├── tests/
│
├── screenshots/
│
├── embedding_service.py
├── requirements.txt
└── README.md
```

---

## Roadmap

### V1 - MVP Funcional ✅

- Consulta em linguagem natural
- Geração de embeddings com Legal-BERT
- Oracle AI Vector Search
- Recuperação dos 5 chunks mais relevantes
- Histórico de consultas
- Integração Oracle APEX

### V2 - Em Desenvolvimento

- Integração com LLM
- Resposta consolidada em linguagem natural
- Exibição das fontes utilizadas
- Resumo contextual dos artigos recuperados

### V3 - Evoluções Futuras

- Feedback dos usuários
- Dashboard de utilização
- Métricas de relevância
- Monitoramento e observabilidade

---

## Aviso

O TributAI possui finalidade educacional e de apoio à pesquisa.

As respostas fornecidas pelo sistema não substituem a análise de profissionais especializados nem a consulta às fontes oficiais da legislação vigente.

---

## Autor

**Helder Costa Amaral**

Projeto desenvolvido como parte do Challenge Alura + Oracle ONE e evoluído para estudo aplicado de IA Generativa, Busca Vetorial e Oracle AI Vector Search.
