# app/chunk_articles.py

import re


def carregar_texto(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def separar_artigos(texto):
    padrao = r'(?=Art\.\s+\d+[º°]?(?:-[A-Z])?)'
    artigos = re.split(padrao, texto)
    return [a.strip() for a in artigos if a.strip()]


def gerar_chunks(caminho):
    texto = carregar_texto(caminho)
    return separar_artigos(texto)


def extrair_artigo(conteudo):
    match = re.match(
      # r"^(Art\.\s+\d+(?:-[A-Z])?[º°]?)",
        r"^(Art\.\s+\d+[º°]?(?:-[A-Z])?)",
        conteudo
    )

    if match:
        return match.group(1)

    return None
