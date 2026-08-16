from db.connection import get_connection


def inserir_documento(nome_documento, total_chunks):

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            id_documento = cur.var(int)

            cur.execute("""
                INSERT INTO TAI_DOCUMENTO_T
                (
                    NOME_DOCUMENTO,
                    TOTAL_CHUNKS,
                    DT_CARGA
                )
                VALUES
                (
                    :1,
                    :2,
                    SYSTIMESTAMP
                )
                RETURNING ID_DOCUMENTO INTO :3
            """, [
                nome_documento,
                total_chunks,
                id_documento
            ])

            conn.commit()

            return id_documento.getvalue()[0]

    finally:
        conn.close()

