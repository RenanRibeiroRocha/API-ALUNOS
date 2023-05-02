from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste@123'

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="db_alunossala"
)

cursor = banco.cursor()


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'usuario.teste' and senha == 'teste@123':
        return render_template("home.html"), 200
    else:
        return render_template("login.html"), 407


@app.route('/alunos', methods=['GET'])
def get_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    return jsonify(alunos)


@app.route('/cadastro/<nome>/<sobrenome>/<curso>', methods=['GET','POST'])
def add_aluno(nome,sobrenome,curso):

    sql = "INSERT INTO alunos (nome, sobrenome, curso) VALUES (%s, %s, %s)"
    val = (nome, sobrenome, curso)
    cursor.execute(sql, val)
    banco.commit()

    return "Aluno cadastrado com sucesso"


@app.route('/apagar/<nome>', methods=['GET','DELETE'])
def del_aluno(nome):

    sql = "DELETE FROM alunos WHERE nome = %s"
    val = (nome,)

    cursor.execute(sql, val)
    banco.commit()

    return "Aluno excluído com sucesso"


if __name__ == "__main__":
    app.run(debug=True)