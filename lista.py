from flask import Flask, request, jsonify

app = Flask(__name__)

itens = [
    {
        "id": 1,
        "nome": "Arroz 5kg",
        "quantidade": 2,
        "categoria": "Alimentação",
        "prioridade": "alta",
        "comprado": False
    }
]

@app.route("/items", methods=["GET"])
def listar_itens():
    return jsonify(itens)

@app.route("/items/<id>", methods=["GET"])
def buscar_item(id):
    item = next((i for i in itens if i["id"] == id), None)
    if not item:
        return jsonify({"erro": "Item não encontrado!"}), 404

        return jsonify(item)

@app.route("/items", methods=["POST"])
def add_item():
    dados = request.get_json()
    novo_item = {
        "id": len(itens) + 1,
        "nome": dados["quantidade"],
        "quantidade": dados["quantidade"],
        "categoria": dados["categoria"],
        "prioridade": dados["prioridade"],
        "comprado": dados["comprado"]
    }
    itens.append(novo_item)
    return jsonify(novo_item), 201