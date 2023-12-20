from flask import Flask, render_template, request
import re
from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Lista para armazenar os exercícios
exercicios = ["", "", "", "", "", "", ""]

def calcular_quantidade(palavras):
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

@app.route("/", methods=['GET', 'POST'])
def planilha_exercicios_page():
    global exercicios

    if request.method == 'POST':
        dia_semana = int(request.form['dia_semana'])
        nome_exercicio = request.form['nome_exercicio']
        exercicios[dia_semana] = nome_exercicio

    # Obter todas as palavras dos exercícios
    palavras = re.findall(r'"([^"]+)"', ' '.join(exercicios))

    # Calcular a quantidade de cada palavra
    contagem = calcular_quantidade(palavras)

    # Criar listas para os dados do gráfico
    labels = list(contagem.keys())
    quantidade = list(contagem.values())

    return render_template("index.html", exercicios=exercicios, labels=labels, quantidade=quantidade)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
