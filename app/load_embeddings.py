# app/load_embeddings.py

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

EMBEDDINGS_DIR = Path("data/embeddings")

conn = get_connection()
cursor = conn.cursor()

total = 0

for arquivo in sorted(EMBEDDINGS_DIR.glob("*_embeddings.json")):

    nome_base = arquivo.name.replace("_embeddings.json", "")
    id_documento = DOC_MAP[nome_base]

    print(f"Processando {arquivo.name}")

    with open(arquivo, encoding="utf-8") as f:
        registros = json.load(f)

    atualizados = 0

    for ordem, item in enumerate(registros, start=1):

        cursor.execute(
            """
            update tai_chunk_t
               set embedding = to_vector(:embedding)
             where id_documento = :id_documento
               and ordem_chunk = :ordem_chunk
            """,
            {
                "embedding": str(item["embedding"]),
                "id_documento": id_documento,
                "ordem_chunk": ordem
            }
        )

        atualizados += cursor.rowcount
        total += cursor.rowcount

    conn.commit()

    print(f"  {atualizados} embeddings carregados")

print("\n" + "=" * 50)
print(f"TOTAL EMBEDDINGS CARREGADOS: {total}")
print("=" * 50)

cursor.close()
conn.close()
