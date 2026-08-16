def inserir_chunks_lote(conn, id_documento, chunks):

    dados = []

    for ordem, chunk in enumerate(chunks, start=1):
        dados.append(
            (
                id_documento,
                None,
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
