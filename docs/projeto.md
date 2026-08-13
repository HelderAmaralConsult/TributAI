# TributAI - Documento de Projeto

## 1. Visão Geral

O TributAI é um assistente inteligente baseado em Inteligência Artificial e técnicas de RAG (Retrieval-Augmented Generation) para consulta de documentos oficiais relacionados à Reforma Tributária Brasileira.

O sistema permitirá que usuários realizem perguntas em linguagem natural e recebam respostas fundamentadas em documentos oficiais previamente indexados.

---

## 2. Objetivo

Facilitar a consulta, estudo e compreensão da legislação e regulamentação da Reforma Tributária Brasileira por meio de uma interface conversacional baseada em IA.

O TributAI deverá recuperar informações presentes em documentos oficiais e apresentar respostas claras, acompanhadas das respectivas fontes.

---

## 3. Público-Alvo

- Estudantes
- Contadores
- Advogados
- Consultores
- Empresários
- Profissionais da área fiscal e tributária
- Interessados na Reforma Tributária

---

## 4. Escopo da Versão 1.0

A primeira versão terá foco na criação de um MVP funcional para atender aos requisitos do Challenge Alura Agente.

### Funcionalidades

- Leitura de documentos PDF
- Indexação dos documentos
- Busca semântica
- Respostas em linguagem natural
- Exibição das fontes utilizadas
- API para consulta

---

## 5. Fontes de Dados Iniciais

### Obrigatórias

- Emenda Constitucional nº 132/2023
- Lei Complementar nº 214/2025

### Futuras

- Notas Técnicas
- Perguntas e Respostas da Receita Federal
- Normativos da Receita Federal
- Publicações do Ministério da Fazenda
- Regulamentações complementares

---

## 6. Arquitetura Prevista

```text
Usuário
   │
   ▼
FastAPI
   │
   ▼
LangChain
   │
   ▼
Retriever
   │
   ▼
ChromaDB
   │
   ▼
Documentos Oficiais
   │
   ▼
Gemini
```

---

## 7. Tecnologias Previstas

### Linguagem

- Python

### IA

- Google Gemini
- LangChain

### Banco Vetorial

- ChromaDB

### API

- FastAPI

### Infraestrutura

- Oracle Cloud Infrastructure (OCI)

### Controle de Versão

- GitHub

---

## 8. Entregáveis do Challenge

### GitHub

- Repositório público
- Histórico de commits
- Código-fonte organizado

### README

- Descrição do projeto
- Arquitetura
- Tecnologias
- Instruções de execução
- Exemplos de perguntas
- Exemplos de respostas

### Agente Funcional

- Processamento de documentos
- Resposta baseada em documentos oficiais

### OCI

- Aplicação implantada
- Link público ou evidência da execução

---

## 9. Cronograma

### Fase 0 - Planejamento

- [x] Definir ideia do projeto
- [x] Definir nome TributAI
- [x] Criar repositório GitHub
- [ ] Definir arquitetura final

### Fase 1 - Preparação

- [ ] Concluir treinamento
- [ ] Criar ambiente de desenvolvimento
- [ ] Organizar documentos oficiais

### Fase 2 - Desenvolvimento

- [ ] Leitura dos PDFs
- [ ] Geração de embeddings
- [ ] Banco vetorial
- [ ] Implementação do RAG

### Fase 3 - API

- [ ] Criar endpoints
- [ ] Testar consultas

### Fase 4 - Deploy

- [ ] Deploy na OCI
- [ ] Testes finais

### Fase 5 - Entrega

- [ ] Revisão do README
- [ ] Capturas de tela
- [ ] Submissão do Challenge

---

## 10. Observações

O TributAI é um projeto educacional desenvolvido como parte do Challenge Alura Agente.

As respostas produzidas pelo sistema possuem caráter informativo e não substituem a consulta às fontes oficiais nem a orientação de profissionais especializados.
