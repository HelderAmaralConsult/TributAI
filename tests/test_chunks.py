from app.chunk_articles import gerar_chunks

chunks = gerar_chunks(
    "data/processed/Lei_Complementar_214.txt"
)

print(len(chunks))
print(chunks[0][:200])

