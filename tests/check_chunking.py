import json

with open(
    "data/embeddings/Lei_Complementar_214_embeddings.json",
    encoding="utf-8"
) as f:
    dados = json.load(f)

for pos, item in enumerate(dados, start=1):
    if item["artigo"] == "Art. 517":
        print(
            pos,
            item["conteudo"][:200]
        )
