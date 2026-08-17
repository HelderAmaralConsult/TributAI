# app/test_vector.py

import json

from db.connection import get_connection

with open(
    "data/embeddings/Lei_Complementar_214_embeddings.json",
    encoding="utf-8"
) as f:
    dados = json.load(f)

embedding = dados[0]["embedding"]

conn = get_connection()
cur = conn.cursor()


embedding = dados[0]["embedding"]

cur.execute(
    """
    update tai_chunk_t
       set embedding = :embedding
     where id_chunk = :id_chunk
    """,
    {
        "embedding": embedding,
        "id_chunk": 6467
    }
)

conn.commit()

print("OK")

cur.close()
conn.close()
