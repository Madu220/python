from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mensagem')
def mensagem():
    return """
    <h1>Comunicação funcionando!</h1>

    <p>
        O HTML enviou uma requisição e o Python respondeu corretamente usando Flask.
    </p>

    <a href="/">Voltar</a>
    """

app.run(debug=True)