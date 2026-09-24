from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Automacao Python rodando perfeitamente!",
        "versao": "1.1.0",
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "teste-automacao"}), 200


@app.route("/api/saudacao", methods=["GET"])
def saudacao():
    nome = request.args.get("nome", "DevOps")
    return jsonify({"mensagem": f"Ola, {nome}! Seja bem-vindo ao pipeline."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # nosec B104
