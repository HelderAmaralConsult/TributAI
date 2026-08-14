import time
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

inicio_total = time.time()

CHUNKS_DIR = Path("data/chunks")
EMBEDDINGS_DIR = Path("data/embeddings")

EMBEDDINGS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


MODEL_NAME = "ulysses-camara/legal-bert-pt-br"


def carregar_chunks(arquivo):
    with open(
        arquivo,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def salvar_embeddings(
    arquivo_saida,
    dados
):
    with open(
        arquivo_saida,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dados,
            f,
            ensure_ascii=False,
            indent=2
        )














def main():

    print("Carregando modelo...")

    model = SentenceTransformer(
        MODEL_NAME
    )

    print("Modelo carregado.\n")

    inicio_total = time.time()

    arquivos_chunks = sorted( CHUNKS_DIR.glob("*_chunks.json") )

    for arquivo_chunks in arquivos_chunks:

        print("\n" + "=" * 60)
        print(f"Processando: {arquivo_chunks.name}")
        print("=" * 60)

        chunks = carregar_chunks(
            arquivo_chunks
        )

        resultado = []

        inicio_arquivo = time.time()

        for i, chunk in enumerate(
            chunks,
            start=1
        ):

            inicio_chunk = time.time()

            embedding = model.encode(
                chunk["conteudo"],
                normalize_embeddings=True
            )

            tempo_chunk = (
                time.time() -
                inicio_chunk
            )

            tempo_medio = (
                (time.time() - inicio_arquivo)
                / i
            )

            restante = (
                len(chunks) - i
            ) * tempo_medio

            percentual = (
                i / len(chunks)
            ) * 100

            resultado.append(
                {
                    "documento":
                        chunk["documento"],

                    "artigo":
                        chunk["artigo"],

                    "tamanho":
                        chunk["tamanho"],

                    "conteudo":
                        chunk["conteudo"],

                    "embedding":
                        embedding.tolist()
                }
            )

            print(
                f"[{i}/{len(chunks)}] "
                f"{percentual:6.2f}% "
                f"{chunk['artigo']} "
                f"({tempo_chunk:.2f}s) "
                f"- ETA: {restante/60:.1f} min"
            )

        nome_saida = (
            arquivo_chunks.name
            .replace("_chunks.json", "_embeddings.json")
        )

        salvar_embeddings(
            EMBEDDINGS_DIR / nome_saida,
            resultado
        )

        tempo_arquivo = (
            time.time() -
            inicio_arquivo
        )

        print(
            f"\nArquivo salvo: {nome_saida}"
        )

        print(
            f"Tempo do arquivo: "
            f"{tempo_arquivo/60:.1f} min"
        )

    tempo_total = (
        time.time() -
        inicio_total
    )

    print("\n" + "=" * 60)
    print("PROCESSAMENTO FINALIZADO")
    print("=" * 60)

    print(
        f"Tempo total: "
        f"{tempo_total/60:.1f} min"
    )
    
    
if __name__ == "__main__":
    main()
