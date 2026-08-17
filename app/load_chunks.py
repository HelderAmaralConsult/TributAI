# app/load_chunks.py

import json
from pathlib import Path

from db.connection import get_connection
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import json

DOC_MAP = {
    "Emenda_Constitucional_132": 64,
    "Lei_Complementar_214": 65,
    "Lei_Complementar_215": 66,
    "Lei_Complementar_216": 67,
    "Lei_Complementar_227": 68,
}

CHUNKS_DIR = Path("data/chunks")

conn = get_connection()
cursor = conn.cursor()

total = 0

for arquivo in sorted(CHUNKS_DIR.glob("*_chunks.json")):

    nome_base = arquivo.name.replace("_chunks.json", "")
    id_documento = DOC_MAP[nome_base]

    print(f"Processando {arquivo.name} -> ID {id_documento}")

    with open(arquivo, encoding="utf-8") as f:
        chunks = json.load(f)

    for chunk in chunks:

        cursor.execute(
            """
            insert into tai_chunk_t (
                id_documento,
                artigo,
                tamanho,
                conteudo
            )
            values (
                :1,
                :2,
                :3,
                :4
            )
            """,
            [
                id_documento,
                chunk["artigo"],
                chunk["tamanho"],
                chunk["conteudo"],
            ],
        )

        total += 1

    conn.commit()

    print(f"  {len(chunks)} chunks carregados")

print()
print("=" * 40)
print(f"TOTAL CARREGADO: {total}")
print("=" * 40)

cursor.close()
conn.close()
