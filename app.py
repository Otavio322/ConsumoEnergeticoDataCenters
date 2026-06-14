from flask import Flask, request, render_template
from classifier import fazer_predicao

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    capacidade_mw = float(request.form['capacidade_mw'])
    eficiencia_energetica = float(request.form['eficiencia_energetica'])
    sistema_resfriamento = int(request.form['sistema_resfriamento'])
    eficiencia_agua = float(request.form['eficiencia_agua'])
    consumo_agua_galoes = float(request.form['consumo_agua_galoes'])

    resultado = fazer_predicao(capacidade_mw, eficiencia_energetica, sistema_resfriamento, eficiencia_agua, consumo_agua_galoes)
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)