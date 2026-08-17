import json

from db.connection import get_connection

with open(
    "data/embeddings/Lei_Complementar_214_embeddings.json",
    encoding="utf-8"
) as f:
    dados = json.load(f)

embedding = dados[0]["embedding"]

embedding_txt = str(embedding)

conn = get_connection()
cur = conn.cursor()

cur.execute(
    """
    update tai_chunk_t
       set embedding = to_vector(:vec)
     where id_chunk = 6467
    """,
    vec=embedding_txt
)

conn.commit()

print("OK")

cur.close()
conn.close()
