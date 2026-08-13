import json
import re
from pathlib import Path

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/chunks")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def carregar_texto(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read()


def separar_artigos(texto):
    """
    Divide o texto mantendo cada artigo como um chunk.
    """

    padrao_split = r'(?=Art\.\s+\d+[º°]?(?:-[A-Z])?)'

    partes = re.split(padrao_split, texto)

    partes = [p.strip() for p in partes if p.strip()]

    return partes


def identificar_artigo(texto_artigo):
    """
    Extrai o número do artigo.
    """

    match = re.search(
        r'(Art\.\s+\d+[º°]?(?:-[A-Z])?)',
        texto_artigo
    )

    if match:
        return match.group(1)

    return "PREAMBULO"


def processar_arquivo(arquivo_txt):
    texto = carregar_texto(arquivo_txt)

    artigos = separar_artigos(texto)

    chunks = []

    for artigo in artigos:

        chunks.append(
            {
                "documento": arquivo_txt.stem,
                "artigo": identificar_artigo(artigo),
                "tamanho": len(artigo),
                "conteudo": artigo,
            }
        )

    return chunks


def salvar_chunks(nome_arquivo, chunks):

    caminho_saida = OUTPUT_DIR / nome_arquivo

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )


def main():

    arquivos = sorted(INPUT_DIR.glob("*.txt"))

    total_chunks = 0

    for arquivo in arquivos:

        print(f"\nProcessando: {arquivo.name}")

        chunks = processar_arquivo(arquivo)

        total_chunks += len(chunks)

        nome_json = arquivo.stem + "_chunks.json"

        salvar_chunks(nome_json, chunks)

        print(
            f"Chunks gerados: {len(chunks)}"
        )

    print("\n==============================")
    print(f"Total de chunks: {total_chunks}")
    print("==============================")


if __name__ == "__main__":
    main()
