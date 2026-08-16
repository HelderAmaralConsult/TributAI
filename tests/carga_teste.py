from db.repositories.documento_repository import inserir_documento
from db.repositories.chunk_repository import inserir_chunk

id_doc = inserir_documento(
    "TESTE",
    2
)

inserir_chunk(
    id_doc,
    "Art.1",
    100,
    "Primeiro chunk",
    1
)

inserir_chunk(
    id_doc,
    "Art.2",
    120,
    "Segundo chunk",
    2
)

print(id_doc)

