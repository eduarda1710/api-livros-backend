from flask import Flask, jsonify, request
app = Flask(__name__)

livros = [
 {"id": 1, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997},
 {"id": 2, "titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844},
 {"id": 3, "titulo": "Clara dos Anjos", "autor": "Lima Barreto", "ano": 1922}
]

@app.route('/livros', methods=['GET'])
def listar_livros():
 return jsonify({"livros": livros})

if __name__ == '__main__':
    app.run(debug=True)