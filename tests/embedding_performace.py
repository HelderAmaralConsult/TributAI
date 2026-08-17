# tests/embedding_performance.py

import time

inicio_total = time.time()
print("INICIO")

t = time.time()
from sentence_transformers import SentenceTransformer
print("IMPORT:", round(time.time() - t, 2))

t = time.time()
model = SentenceTransformer(
    "ulysses-camara/legal-bert-pt-br"
)
print("MODELO:", round(time.time() - t, 2))

pergunta = "Qual e a aliquota reduzida para medicamentos?"

t = time.time()
embedding = model.encode(
    pergunta,
    normalize_embeddings=True
)
print("EMBEDDING:", round(time.time() - t, 2))

t = time.time()
print(len(embedding))
print("PRINT:", round(time.time() - t, 2))

print("TOTAL:", round(time.time() - inicio_total, 2))

