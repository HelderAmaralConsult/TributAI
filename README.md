# TributAI

Assistente inteligente baseado em IA para consulta da Reforma Tributária Brasileira utilizando RAG (Retrieval-Augmented Generation) e documentos oficiais.

## Sobre o Projeto

O TributAI é um agente de Inteligência Artificial desenvolvido para facilitar a consulta e compreensão da legislação relacionada à Reforma Tributária Brasileira.

O projeto utilizará documentos oficiais públicos, como:

- Emenda Constitucional nº 132/2023
- Lei Complementar nº 214/2025
- Normativos da Receita Federal
- Notas Técnicas
- Guias e publicações oficiais
- Regulamentações complementares

A proposta é permitir que usuários realizem perguntas em linguagem natural e recebam respostas fundamentadas nos documentos oficiais indexados pelo sistema.

## Objetivo

Reduzir o tempo gasto na busca e interpretação de informações relacionadas à Reforma Tributária, oferecendo uma experiência de consulta simples, rápida e baseada em fontes confiáveis.

## Funcionalidades Planejadas

- Consulta em linguagem natural
- Busca semântica em documentos oficiais
- Respostas fundamentadas em fontes oficiais
- Exibição das referências utilizadas
- API para integração com outras aplicações
- Implantação em ambiente Oracle Cloud Infrastructure (OCI)

## Arquitetura (Planejada)

```text
Usuário
   │
   ▼
API (FastAPI)
   │
   ▼
LangChain
   │
   ▼
Retriever
   │
   ▼
Banco Vetorial (ChromaDB)
   │
   ▼
Documentos Oficiais
   │
   ▼
Modelo de Linguagem (LLM)
```
## Tecnologias Previstas
Python
LangChain
ChromaDB
FastAPI
Google Gemini
Docker
Oracle Cloud Infrastructure (OCI)
GitHub

## Estrutura Inicial do Projeto
```text
1 TributAI/
     │
2    ├── docs/
3    ├── app/
4    ├── tests/
5    ├── screenshots/
6    ├── requirements.txt
7    └── README.md


```
## Status do Projeto

🚧 Em desenvolvimento.

Atualmente o projeto encontra-se na fase de planejamento e definição da arquitetura da solução.

## Roadmap
Fase 1 - Planejamento
 Definição da ideia
 Definição do escopo
 Criação do repositório GitHub
 Definição da arquitetura
Fase 2 - Protótipo Local
 Leitura dos documentos
 Processamento dos PDFs
 Geração de embeddings
 Criação da base vetorial
 Implementação do agente RAG
Fase 3 - API
 Criação da API com FastAPI
 Testes locais
Fase 4 - Deploy
 Publicação na OCI
 Testes em ambiente cloud
 Evidências de funcionamento
Aviso

O TributAI tem finalidade educacional e de apoio à pesquisa. As respostas fornecidas pelo sistema não substituem a análise de profissionais especializados nem a consulta às fontes oficiais da legislação vigente.

## Autor

Helder Costa Amaral

Projeto desenvolvido como parte do Challenge Alura-Oracle ONE.
