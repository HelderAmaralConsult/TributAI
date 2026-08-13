import json
from pathlib import Path

CHUNKS_DIR = Path("data/chunks")


def carregar_chunks():
    todos_chunks = []

    for arquivo in sorted(CHUNKS_DIR.glob("*_chunks.json")):
        with open(arquivo, "r", encoding="utf-8") as f:
            chunks = json.load(f)

            for chunk in chunks:
                chunk["arquivo_origem"] = arquivo.name

            todos_chunks.extend(chunks)

    return todos_chunks


def main():
    chunks = carregar_chunks()

    if not chunks:
        print("Nenhum chunk encontrado.")
        return

    tamanhos = [chunk["tamanho"] for chunk in chunks]

    total_chunks = len(chunks)

    tamanho_medio = sum(tamanhos) / total_chunks

    maior_chunk = max(chunks, key=lambda c: c["tamanho"])

    menor_chunk = min(chunks, key=lambda c: c["tamanho"])

    print("=" * 60)
    print("ESTATÍSTICAS DOS CHUNKS")
    print("=" * 60)

    print(f"Total de chunks: {total_chunks}")
    print(f"Tamanho médio: {tamanho_medio:.2f} caracteres")
    print(f"Menor chunk: {menor_chunk['tamanho']} caracteres")
    print(f"Maior chunk: {maior_chunk['tamanho']} caracteres")

    print("\nMaior chunk:")
    print(f"Documento: {maior_chunk['documento']}")
    print(f"Artigo: {maior_chunk['artigo']}")

    print("\nMenor chunk:")
    print(f"Documento: {menor_chunk['documento']}")
    print(f"Artigo: {menor_chunk['artigo']}")

    print("\nTop 10 maiores chunks")
    print("-" * 60)

    top_10 = sorted(
        chunks,
        key=lambda c: c["tamanho"],
        reverse=True
    )[:10]

    for i, chunk in enumerate(top_10, start=1):
        print(
            f"{i:2d}. "
            f"{chunk['documento']} | "
            f"{chunk['artigo']} | "
            f"{chunk['tamanho']} caracteres"
        )


if __name__ == "__main__":
    main()

