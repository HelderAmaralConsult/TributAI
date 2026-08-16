# app/load_document_to_oracle.py

from pathlib import Path

from app.chunk_articles import gerar_chunks
from app.chunk_articles import extrair_artigo
from db.connection      import get_connection


ARQUIVO = "data/processed/Lei_Complementar_214.txt"


def carregar_documento():

    chunks = gerar_chunks(ARQUIVO)

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
                Path(ARQUIVO).stem,
                len(chunks),
                id_documento
            ])

            doc_id = id_documento.getvalue()[0]

            dados = []

            for ordem, chunk in enumerate(chunks, start=1):
                artigo = extrair_artigo(chunk)
                dados.append(
                (
                    doc_id,
                    artigo,
                    len(chunk),
                    chunk,
                    ordem
                )
                )

            cur.executemany("""
                INSERT INTO TAI_CHUNK_T
                (
                    ID_DOCUMENTO,
                    ARTIGO,
                    TAMANHO,
                    CONTEUDO,
                    ORDEM_CHUNK
                )
                VALUES
                (
                    :1,
                    :2,
                    :3,
                    :4,
                    :5
                )
            """, dados)

        conn.commit()

        print(f"Documento criado: {doc_id}")
        print(f"Chunks gravados: {len(chunks)}")

    finally:
        conn.close()


if __name__ == "__main__":
    carregar_documento()

