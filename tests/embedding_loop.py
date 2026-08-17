# tests/embedding_loop.py

from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer(
    "ulysses-camara/legal-bert-pt-br"
)

print("Modelo carregado")

while True:

    pergunta = input("> ")

    inicio = time.time()

    embedding = model.encode(
        pergunta,
        normalize_embeddings=True
    )

    print(
        "Tempo:",
        round(time.time() - inicio, 2)
    )
    print(str(embedding.tolist()))
