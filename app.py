from flask import Flask, request, jsonify
import mysql.connector
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configuração do banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_python"
)
cursor = db.cursor()

# Configuração do JWT
app.config["JWT_SECRET_KEY"] = "minha_chave_secreta"  # Troque por algo mais seguro
jwt = JWTManager(app)

# Função para criptografar senha
def hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Função para verificar senha
def verificar_senha(senha, hash_senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))

# Rota para cadastrar um usuário (Signup)
@app.route('/signup', methods=['POST'])
def signup():
    dados = request.json
    nome = dados['nome']
    email = dados['email']
    senha = hash_senha(dados['senha'])

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        db.commit()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"erro": "Erro ao cadastrar usuário", "detalhe": str(err)}), 400

# Rota para login (gera um token JWT)
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados['email']
    senha = dados['senha']

    cursor.execute("SELECT id, nome, senha FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    if usuario and verificar_senha(senha, usuario[2]):
        token = create_access_token(identity={"id": usuario[0], "nome": usuario[1]})
        return jsonify({"mensagem": "Login bem-sucedido!", "token": token})
    
    return jsonify({"erro": "E-mail ou senha inválidos"}), 401

# Rota protegida para obter informações do usuário logado
@app.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    usuario = get_jwt_identity()
    return jsonify({"mensagem": "Usuário autenticado", "dados": usuario})

if __name__ == '__main__':
    app.run(debug=True)
