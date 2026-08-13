import json
import re
from pathlib import Path

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/chunks")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def carregar_texto(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def separar_artigos(texto):
    """
    Divide o texto em artigos.
    """

    padrao = r'(?=Art\.\s+\d+[º°]?(?:-[A-Z])?)'

    artigos = re.split(padrao, texto)

    return [
        artigo.strip()
        for artigo in artigos
        if artigo.strip()
    ]


def identificar_artigo(texto):
    """
    Extrai o identificador do artigo.
    """

    match = re.search(
        r'(Art\.\s+\d+[º°]?(?:-[A-Z])?)',
        texto
    )

    if match:
        return match.group(1)

    return "PREAMBULO"


def separar_anexos(documento, artigo_id, conteudo):
    """
    Se houver anexos dentro do chunk,
    cria chunks independentes para cada anexo.
    """

    padrao_anexo = r'(?=ANEXO\s+[IVXLCDM]+)'

    partes = re.split(
        padrao_anexo,
        conteudo
    )

    if len(partes) == 1:
        return [{
            "documento": documento,
            "artigo": artigo_id,
            "tamanho": len(conteudo),
            "conteudo": conteudo,
        }]

    chunks = []

    texto_artigo = partes[0].strip()

    if texto_artigo:
        chunks.append({
            "documento": documento,
            "artigo": artigo_id,
            "tamanho": len(texto_artigo),
            "conteudo": texto_artigo,
        })

    for anexo in partes[1:]:

        anexo = anexo.strip()

        match = re.match(
            r'(ANEXO\s+[IVXLCDM]+)',
            anexo
        )

        if match:
            nome_anexo = match.group(1)
        else:
            nome_anexo = "ANEXO"

        chunks.append({
            "documento": documento,
            "artigo": nome_anexo,
            "tamanho": len(anexo),
            "conteudo": anexo,
        })

    return chunks


def processar_arquivo(arquivo_txt):

    texto = carregar_texto(arquivo_txt)

    artigos = separar_artigos(texto)

    chunks = []

    for artigo in artigos:

        artigo_id = identificar_artigo(artigo)

        chunks.extend(
            separar_anexos(
                arquivo_txt.stem,
                artigo_id,
                artigo
            )
        )

    return chunks


def salvar_chunks(nome_arquivo, chunks):

    caminho_saida = OUTPUT_DIR / nome_arquivo

    with open(
        caminho_saida,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )


def main():

    arquivos = sorted(
        INPUT_DIR.glob("*.txt")
    )

    total_chunks = 0

    for arquivo in arquivos:

        print(f"\nProcessando: {arquivo.name}")

        chunks = processar_arquivo(arquivo)

        total_chunks += len(chunks)

        nome_saida = (
            arquivo.stem +
            "_chunks.json"
        )

        salvar_chunks(
            nome_saida,
            chunks
        )

        print(
            f"Chunks gerados: {len(chunks)}"
        )

    print("\n==============================")
    print(f"Total de chunks: {total_chunks}")
    print("==============================")


if __name__ == "__main__":
    main()
