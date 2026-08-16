from db.connection import get_connection
from db.repositories.chunk_repository import inserir_chunks_lote

conn = get_connection()

try:

    chunks = gerar_chunks(
        "data/processed/Lei_Complementar_214.txt"
    )

    inserir_chunks_lote(
        conn,
        id_documento,
        chunks
    )

    conn.commit()

finally:
    conn.close()
