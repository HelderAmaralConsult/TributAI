from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "ulysses-camara/legal-bert-pt-br"
)

#pergunta = """Quais são as regras tributárias para medicamentos?"""
pergunta = """Qual a alíquota para medicamentos?"""

embedding = model.encode(
    pergunta,
    normalize_embeddings=True
)

print(str(embedding.tolist()))
#print(len(embedding))


