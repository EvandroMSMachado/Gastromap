from flask import Flask, request, jsonify
import mysql.connector, sqlite3
colunas = []


app = Flask(__name__)

def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  # "Emsm@1010"
        database="db_gastromap"
    )
    return conn

@app.route("/")
def index():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    conn.close()
    return f"Conectado ao banco de dados: {db_name[0]}"

# ROTA PARA CRIAR UM NOVO PACIENTE
@app.route("/patient", methods=["POST"])
def create_patient():
    conn = connection()
    cursor = conn.cursor()

    data = request.get_json()
    print("Data received:", data)  # Adicione esta linha para depurar

    name = data.get("name")
    password = data.get("password")

    if name and password:
        cursor.execute(
            "INSERT INTO patient (name, password) VALUES (%s, %s)",
            (name, password),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Paciente criado com sucesso"}), 201
    else:
        conn.close()
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400
    
#ROTA PARA CADASTRAR UM NOVO COLABORADOR
@app.route("/employer", methods=["POST"])
def create_employer():
    conn = connection()
    cursor = conn.cursor()

    data = request.get_json()
    print("Data received:", data)  # Adicione esta linha para depurar

    name = data.get("name")
    password = data.get("password")
    email = data.get("email")

    if name and password and email:
        cursor.execute(
            "INSERT INTO employers (name, password, email) VALUES (%s, %s, %s)",
            (name, password, email),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Colaborador criado com sucesso"}), 201
    else:
        conn.close()
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400
    
#ROTA PARA CADASTRAR UMA TABELA DE ALIMENTOS
@app.route("/form", methods=["POST"])
def create_form():
    conn = connection()
    cursor = conn.cursor()

    data = request.get_json()
    print("Data received:", data)  # Adicione esta linha para depurar

    id_patient = data.get("id_patient")
    uva = data.get("uva")
    tapioca = data.get("tapioca")
    requeijao = data.get("requeijao")
    tomate = data.get("tomate")
    repolho = data.get("repolho")
    sorv_picole = data.get("sorv_picole")
    salgadinho = data.get("salgadinho")
    energeticos = data.get("energeticos")

    if uva and tapioca and requeijao and tomate and repolho and sorv_picole and salgadinho and energeticos:
        cursor.execute(
            "INSERT INTO form (id_patient, uva, tapioca, requeijao, tomate, repolho, sorv_picole, salgadinho, energeticos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (id_patient, uva, tapioca, requeijao, tomate, repolho, sorv_picole, salgadinho, energeticos),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Respostas recebidas com sucesso"}), 201
    else:
        conn.close()
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400



@app.route("/colunas/<int:id>", methods=["GET"])
def consulta_nomes(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM form WHERE id_patient = %s', (id,))
    resultados = cursor.fetchall()
    colunas = [item[0] for item in cursor.description]
    resultado = [dict(zip(colunas, paciente)) for paciente in resultados]
    # Feche a conexão com o banco de dados
    conn.close()
    # Exiba o array com os nomes das colunas
    return jsonify(resultado), 200

# import mysql.connector

# def consulta_colunas_por_id(id_especifico):
#     # Conexão com o banco de dados
#     conn = connection()
#     cursor = conn.cursor(dictionary=True)  # cursor em modo dicionário

#     # Execute uma consulta para obter os dados da linha com o id específico
#     query = "SELECT * FROM form WHERE id = %s"
#     cursor.execute(query, (id_especifico,))

#     # Obtenha os nomes das colunas da tabela
#     colunas = [description[0] for description in cursor.description]

#     # Obtenha a linha correspondente ao id específico
#     linha = cursor.fetchone()

#     if linha is None:
#         print(f"Nenhuma linha encontrada com o ID {id_especifico}.")
#     else:
#         # Verifica as colunas a partir da segunda coluna
#         for coluna in colunas[1:]:
#             valor = linha[coluna]  # Obtém o valor da coluna atual para a linha

#             if valor is not None:
#                 continue  # Se o valor não for nulo, pula para a próxima coluna
#             else:
#                 # Se o valor for nulo, imprime o ID no terminal
#                 print(f"ID {id_especifico}: A coluna '{coluna}' tem valor nulo.")

#     # Feche a conexão com o banco de dados
#     conn.close()

# # Solicita o ID específico ao usuário
# id_especifico = input("Informe o ID da linha que deseja verificar: ")

# # Chama a função para executar a consulta e verificação
# consulta_colunas_por_id(id_especifico)


if __name__ == "__main__":
    app.run(debug=True)