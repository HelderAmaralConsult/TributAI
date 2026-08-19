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

Situação do TributAI ao encerrar o dia

✅ Escolheu um tema

✅ Definiu um nome

✅ Levantou requisitos

✅ Pensou na documentação

✅ Entendeu os critérios de avaliação

✅ Está preocupado com o deploy

---

## 2026-08-14

### Escolha do Modelo de Embeddings

Após análise das opções disponíveis, foi escolhido:

```text
ulysses-camara/legal-bert-pt-br

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


## 2026-08-15
### Mudança de planos
Criei um novo banco com ATP ativo, o anterior era específico do APEX.
Com o banco ATP passou a aceitar conexões externas e a carga de documentos e chunks foram via python oracledb e não mais por ORDS.

Assim, as tabelas foram carregadas.

### Investigação da busca vetorial

Foram realizados diversos testes para validar a qualidade dos embeddings carregados no Oracle e a correspondência entre chunks e vetores.

Principais atividades:

- Teste com o Art. 4º da LC 214.
- Geração do embedding diretamente a partir do texto do artigo.
- Validação da recuperação vetorial.
- Investigação dos artigos 132 a 142, que possuem conteúdo extremamente semelhante.
- Investigação do Art. 517 e da estrutura de chunking utilizada na carga.

### Resultados

O Art. 4º foi recuperado corretamente em primeiro lugar a partir do seu próprio embedding.

Foram identificados diversos artigos com alta similaridade semântica, especialmente na região dos artigos 129 a 142 da LC 214, o que influencia o ranking dos resultados.

Durante a análise do Art. 517 foi constatado que o trecho pesquisado não estava presente no chunk correspondente armazenado no banco, o que invalidava aquele teste específico de recuperação.

### Atividades realizadas

- Realizados diversos testes de validação dos embeddings carregados no Oracle.
- Investigada a hipótese de desalinhamento entre chunks e embeddings durante a carga.
- Testado o Art. 4º da LC 214 como caso de controle. Analisada a estrutura de chunks da LC 214.
- Confirmado que a busca vetorial retorna o próprio Art. 4º na primeira posição.
- Investigados os resultados obtidos para os artigos 133, 132, 137, 138, 139, 140, 141 e 142.
- Verificado que esses artigos possuem textos extremamente semelhantes, o que influencia o ranking semântico.
- Identificada a existência de artigos divididos em múltiplos chunks.

### Conclusões

- Não foram encontradas evidências de deslocamento global entre chunks e embeddings.
- Os embeddings parecem estar associados aos registros corretos.
- A estrutura de carga aparentava estar correta.
- Permaneceram dúvidas sobre a qualidade semântica do modelo utilizado para embeddings.
- A principal limitação observada está relacionada à qualidade da recuperação semântica do modelo utilizado.
- A investigação de melhorias semânticas ficou registrada como evolução futura do projeto.
---

## 2026-08-16

### Validação definitiva dos embeddings

Foi realizado um teste utilizando o conteúdo completo do chunk 6690 (Art. 133).

Procedimento:

- Extração do conteúdo armazenado no banco.
- Geração de um novo embedding utilizando o mesmo modelo empregado durante a carga.
- Comparação do vetor gerado com os embeddings armazenados no Oracle AI Vector Search.

Resultado obtido:
Art. 133
Distância ≈ 0
Posição = 1

### Serviço de geração de embeddings

Foi identificado que a geração de embeddings diretamente por execução de scripts Python não era adequada para uso em produção.

Durante os testes, observou-se que cada execução do processo precisava:

- Inicializar o ambiente Python.
- Carregar as bibliotecas do projeto.
- Carregar o modelo Legal-BERT.
- Processar a pergunta recebida.

Esse processo adicionava uma latência significativa à consulta, tornando inviável a geração de embeddings sob demanda para utilização pelo APEX.

### Solução adotada

Foi criada uma API REST utilizando Flask para manter o modelo carregado em memória durante toda a execução da aplicação.

Arquivo criado:
app/embedding_service.py

### Endpoints disponibilizados:

GET  /health
POST /embed

O endpoint /embed recebe uma pergunta em formato JSON e retorna o embedding correspondente.
Exemplo:
{
  "pergunta": "Qual a alíquota para medicamentos?"
}
Retorno:
{
  "embedding": [...]
}


### Testes de desempenho

Foram realizados testes comparando a execução isolada do modelo e a execução através da API.

Resultados observados:

Primeira execução: aproximadamente 6 segundos.
Segunda execução: aproximadamente 2 segundos.
Consultas subsequentes: praticamente instantâneas.

A melhoria ocorreu porque o modelo permanece carregado em memória, eliminando o custo de inicialização a cada consulta.

Implantação com Gunicorn

Para utilização em ambiente de produção, o Flask passou a ser executado através do Gunicorn.

Comando utilizado:
gunicorn \
  --bind 0.0.0.0:5000 \
  --workers 1 \
  app.embedding_service:app

Benefícios:

Processo persistente.
Maior estabilidade.
Melhor integração com o sistema operacional.
Possibilidade de reinicialização automática em caso de falha.

### Configuração do serviço do sistema

Foi criado o serviço:
tributai-embedding.service
utilizando o systemd.

Objetivos:

Inicialização automática durante o boot da VM.
Reinicialização automática em caso de falha.
Execução contínua do serviço de embeddings sem intervenção manual.

Status final do serviço:
   Active: active (running)
   Enabled: yes

### Arquitetura definida para consulta
APEX
 ↓
REST /embed
 ↓
Gunicorn
 ↓
Flask
 ↓
Legal-BERT carregado em memória
 ↓
Embedding
 ↓
Oracle AI Vector Search
 ↓
Resultados



Situação do TributAI ao encerrar o dia

✅ Embeddings gerados

✅ Embeddings carregados no Oracle

✅ Busca vetorial validada

✅ Sincronismo chunk ↔ embedding validado

✅ Flask implementado

✅ Endpoint /embed

✅ Endpoint /health

✅ Gunicorn configurado

✅ Systemd configurado

✅ Inicialização automática no boot

✅ Commit realizado

✅ Push realizado

✅ Diário de bordo atualizado

## 17/08/2026

### Objetivo
Preparar e validar o serviço de geração de embeddings para integração com o Oracle AI Vector Search.

### Atividades realizadas
- Implantação do serviço de embeddings baseado em Flask.
- Configuração do Gunicorn para execução em modo serviço.
- Configuração do serviço systemd para inicialização automática.
- Validação do carregamento do modelo Legal-BERT.
- Implementação do endpoint /embed para geração de embeddings.
- Implementação do endpoint /health para monitoramento do serviço.
- Testes de geração de embeddings via curl e Python.
- Ajustes de estrutura do projeto e organização dos componentes de backend.

### Resultados
- Serviço de embeddings executando de forma persistente.
- Endpoint /health retornando status operacional.
- Endpoint /embed gerando embeddings compatíveis com Oracle VECTOR.
- Integração entre Legal-BERT e Flask validada.
- Ambiente preparado para integração com o Oracle Autonomous Database.

### Arquitetura validada

✅ Legal-BERT

✅ Flask

✅ Gunicorn

✅ Systemd

✅ Endpoint REST /embed

✅ Backend de Embeddings

✅ Legal-BERT

✅ Flask

✅ Gunicorn

## 18/08/2026

### Objetivo
Concluir a integração entre o APEX e o serviço de geração de embeddings.

### Atividades realizadas
- Validação do serviço Flask/Gunicorn em execução na OCI.
- Diagnóstico das restrições de acesso do APEX ao endpoint HTTP.
- Identificação de bloqueio por HTTPS obrigatório (ORA-20987).
- Instalação e configuração do Nginx.
- Investigação de conectividade OCI (VCN, Security Lists, Route Table e Public IP).
- Identificação de regras restritivas no iptables da VM.
- Liberação das portas 80, 443 e 5000.

### Resultados
- Endpoint Flask acessível externamente.
- Nginx publicado com sucesso.
- Infraestrutura preparada para HTTPS.

✅ Infraestrutura

✅ OCI

✅ Firewall

✅ Nginx

✅ HTTPS

## 19/08/2026

### Objetivo
Finalizar a integração APEX + Embeddings + Oracle AI Vector Search.

### Atividades realizadas
- Criação do domínio público tributai.duckdns.org.
- Configuração de HTTPS utilizando Let's Encrypt e Certbot.
- Configuração do Nginx como proxy reverso para o serviço Flask.
- Validação de acesso HTTPS pelo APEX.
- Criação do REST Data Source para o endpoint /embed.
- Implementação do processo PRC_PESQUISAR.
- Consumo de embeddings via Legal-BERT.
- Conversão do vetor para Oracle VECTOR.
- Implementação da busca vetorial utilizando VECTOR_DISTANCE.
- Implementação do histórico de consultas.
- Registro do ID_CHUNK_TOP1 para auditoria de resultados.

### Resultados
- Integração ponta a ponta concluída.
- Consulta em linguagem natural funcionando.
- Recuperação dos 5 chunks mais relevantes da legislação.
- Histórico de consultas persistido em banco.
- Primeira versão funcional do TributAI concluída.

### Arquitetura validada

✅ Integração Completa

✅ APEX

✅ Embedding

✅ Oracle AI Vector Search

✅ Top 5 Chunks

✅ Histórico

✅ Fechando o pacote

✅ Atualizando o GitHub
