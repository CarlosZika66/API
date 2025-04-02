from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/idade', methods=['POST'])
def VerificarIdade():
    dados = request.get_json()

    if not dados or "idade" not in dados:
        return jsonify({"Erro": "Envie a idade no JSON"}), 400
    
    idade = dados["idade"]

    if not isinstance(idade, (int, float)):
        return jsonify({'Erro: a idade deve ser apenas numero'}), 400
    
    res = idade

    if res <= 17:
        return jsonify({'mensagem': 'VOCE E DE MENOR'}), 200
    elif res >= 18:
        return jsonify({'mensagem':'VOCE E MAIOR DE IDADE'}), 200

if __name__ == '__main__':
    app.run(debug=True)
