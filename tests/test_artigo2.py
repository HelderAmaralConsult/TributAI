# tests/test_artigo.py

from app.chunk_articles import gerar_chunks
from app.chunk_articles import extrair_artigo

chunks = gerar_chunks(
    "data/processed/Lei_Complementar_214.txt"
)

for chunk in chunks[1:10]:
    print(extrair_artigo(chunk))
