# Embeddings

## Modelo Escolhido

```text
ulysses-camara/legal-bert-pt-br
```

Biblioteca:

```python
from sentence_transformers import SentenceTransformer
```

---

## Motivação

O TributAI trabalha com:

- legislação
- português brasileiro
- reforma tributária

Por esse motivo foi escolhido um modelo especializado em domínio jurídico.

---

## Carregamento do Modelo

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "ulysses-camara/legal-bert-pt-br"
)
```

---

## Geração de Embedding

```python
embedding = model.encode(
    "O IBS é um imposto sobre bens e serviços.",
    normalize_embeddings=True
)
```

---

## Dimensionalidade

Teste realizado:

```python
print(embedding.shape)
```

Resultado:

```text
(768,)
```

Portanto cada embedding possui:

```text
768 dimensões
```

---

## Testes de Similaridade

### Caso Jurídico Relacionado

```text
IBS
```

vs

```text
Imposto sobre Bens e Serviços
```

Resultado:

```text
0.3968
```

---

### Caso Sem Relação Semântica

```text
IBS
```

vs

```text
Receita de bolo de chocolate
```

Resultado:

```text
0.0285
```

---

## Base Gerada

### Chunks

```text
1172
```

### Arquivos de Embeddings

```text
Emenda_Constitucional_132_embeddings.json

Lei_Complementar_214_embeddings.json

Lei_Complementar_215_embeddings.json

Lei_Complementar_216_embeddings.json

Lei_Complementar_227_embeddings.json
```

### Tempo de Processamento

```text
11.3 minutos
```

### Espaço Utilizado

```text
42 MB
```

---

## Status

```text
✅ Embeddings gerados

✅ Modelo validado

✅ Similaridade semântica validada

⬜ Oracle Vector Search

⬜ Recuperação vetorial

⬜ RAG completo
```
