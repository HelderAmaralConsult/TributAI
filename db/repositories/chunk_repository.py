# db/repositories/chunk_repository.py

from app.chunk_articles import extrair_artigo


def inserir_chunks_lote(conn, id_documento, chunks):

    dados = []

    for ordem, chunk in enumerate(chunks, start=1):

        artigo = extrair_artigo(chunk)

        print(f"ARTIGO={artigo}")

        dados.append(
            (
                id_documento,
                artigo,
                len(chunk),
                chunk,
                ordem
            )
        )

    with conn.cursor() as cur:

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
