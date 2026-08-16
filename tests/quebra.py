from app.chunk_articles import gerar_chunks

chunks = gerar_chunks(
    "data/processed/Lei_Complementar_214.txt"
)

print(chunks[0][:500])

print("\n-------------------\n")

print(chunks[1][:500])
