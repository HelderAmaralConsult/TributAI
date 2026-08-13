import re
from pathlib import Path

# Arquivo que será analisado
ARQUIVO = "data/processed/Lei_Complementar_214.txt"


def carregar_texto(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def separar_artigos(texto):
    """
    Divide o texto em chunks baseados em artigos.

    Exemplos capturados:
    Art. 1º
    Art. 7º-A
    Art. 10.
    Art. 156-A
    """

    padrao = r'(?=Art\.\s+\d+[º°]?(?:-[A-Z])?)'

    artigos = re.split(padrao, texto)

    artigos = [a.strip() for a in artigos if a.strip()]

    return artigos


def main():
    texto = carregar_texto(ARQUIVO)

    artigos = separar_artigos(texto)

    print("=" * 60)
    print(f"Documento: {Path(ARQUIVO).name}")
    print(f"Artigos encontrados: {len(artigos)}")
    print("=" * 60)

    print("\nPrimeiros 5 artigos:\n")

    for i, artigo in enumerate(artigos[:5], start=1):
        print(f"--- CHUNK {i} ---")
        print(f"Tamanho: {len(artigo)} caracteres")
        print(artigo[:500])
        print("\n")


if __name__ == "__main__":
    main()
