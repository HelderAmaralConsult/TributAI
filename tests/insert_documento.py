# tests/insert_documento.py

from db.connection import get_connection

conn = get_connection()

with conn.cursor() as cur:

    cur.execute("""
        INSERT INTO TAI_DOCUMENTO_T (
            NOME_DOCUMENTO,
            TOTAL_CHUNKS,
            DT_CARGA
        )
        VALUES (
            :1,
            :2,
            SYSTIMESTAMP
        )
        RETURNING ID_DOCUMENTO INTO :3
    """,
    [
        "LC_214_2025.pdf",
        0,
        cur.var(int)
    ])

    id_documento = cur.getimplicitresults()

conn.commit()
conn.close()

