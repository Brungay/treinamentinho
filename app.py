from flask import Flask, render_template, request
import pandas as pd
from unidecode import unidecode

app = Flask(__name__)

# Carregar o DataFrame no escopo global
tabela = pd.read_excel(r'C:\Users\Usuario\Desktop\Treinamento\Taco.xlsx')

def remover_acentos(texto):
    return unidecode(texto)

def pesquisar_por_palavra(chave):
    chave_sem_acentos = remover_acentos(chave.lower())
    palavras_chave = chave_sem_acentos.split()

    # Inicializa uma Series de booleanos para verificar se cada palavra está presente em alguma coluna
    condicoes = tabela.apply(lambda row: all(palavra in str(row).lower() for palavra in palavras_chave), axis=1)

    # Aplica as condições para obter o resultado final
    resultado_pesquisa = tabela[condicoes]
    return resultado_pesquisa

@app.route("/", methods=['POST', 'GET'])
def home():
    alimento_desejado = ""  # Move a declaração para fora do bloco condicional
    resultado_pesquisa = None

    if request.method == 'POST':
        alimento_desejado = request.form.get('name', '')
        resultado_pesquisa = pesquisar_por_palavra(alimento_desejado)

    return render_template("index.html", name=alimento_desejado, resultado_pesquisa=resultado_pesquisa)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
