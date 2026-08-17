from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

print("Carregando modelo...")

model = SentenceTransformer(
    "ulysses-camara/legal-bert-pt-br"
)

print("Modelo carregado")


@app.route("/embed", methods=["POST"])
def embed():

    dados = request.get_json()

    pergunta = dados["pergunta"]

    embedding = model.encode(
        pergunta,
        normalize_embeddings=True
    )

    return jsonify({
        "embedding": embedding.tolist()
    })


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
