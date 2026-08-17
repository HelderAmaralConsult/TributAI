# app/fill_ordem_chunk.py

import json
from pathlib import Path

from db.connection import get_connection

DOC_MAP = {
    "Emenda_Constitucional_132": 64,
    "Lei_Complementar_214": 65,
    "Lei_Complementar_215": 66,
    "Lei_Complementar_216": 67,
    "Lei_Complementar_227": 68,
}

CHUNKS_DIR = Path("data/chunks")

conn = get_connection()
cursor = conn.cursor()

total = 0

for arquivo in sorted(CHUNKS_DIR.glob("*_chunks.json")):

    nome_base = arquivo.name.replace("_chunks.json", "")
    id_documento = DOC_MAP[nome_base]

    print(f"Processando {arquivo.name}")

    with open(arquivo, encoding="utf-8") as f:
        chunks = json.load(f)

    for ordem, chunk in enumerate(chunks, start=1):

        cursor.execute(
            """
            update tai_chunk_t
               set ordem_chunk = :ordem
             where id_documento = :id_documento
               and artigo = :artigo
               and conteudo = :conteudo
            """,
            {
                "ordem": ordem,
                "id_documento": id_documento,
                "artigo": chunk["artigo"],
                "conteudo": chunk["conteudo"],
            }
        )

        total += cursor.rowcount

    conn.commit()

print()
print("=" * 40)
print(f"TOTAL ATUALIZADO: {total}")
print("=" * 40)

cursor.close()
conn.close()
