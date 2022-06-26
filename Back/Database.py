from flask import Flask, request as flask_request
import sqlite3 as sql
import os
import Crypt

app = Flask(__name__)

os.environ['DBPATH'] = 'database.db'


def cadastro_users(json_data):
        password = Crypt.encrypt(json_data["pass"])

        try:
            conn = sql.connect(os.environ['DBPATH'])
            cur = conn.cursor()
            cur.execute(f'INSERT INTO users (email, CPF, password) VALUES ("{json_data["email"]}", "{json_data["cpf"]}", "{password}")')
            conn.commit()

            return f'Inserido com o email: {json_data["email"]}, cpf: {json_data["cpf"]} e senha: password: {password}'

        except Exception as e:
            return(str(e))


def login(json_data):
        try:
            conn = sql.connect(os.environ['DBPATH'])
            cur = conn.cursor()
            cur.execute(f'Select password from users where email={json_data["email"]}')
            password = Crypt.decrypt(cur.fetchone()[0])
            print(type(password))

        except Exception as e:
            return(str(e))


def createdb():
    if not os.path.exists(os.environ['DBPATH']):
        conn = sql.connect(os.environ['DBPATH'])
        conn.execute(
            'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN, icon TEXT, email TEXT, password BLOB, CPF INTEGER)')
        conn.commit()
        conn.close()
        app.logger.info('Database created')
        return 'Database created'
    else:
        return 'Database already exists'

@app.route('/cadastro/usuarios', methods=['POST'])
def cadastro_usuarios():
    json_data = flask_request.get_json()
    if json_data:
        return cadastro_users(json_data)


@app.route('/login', methods=['POST'])
def dologin():
    json_data = flask_request.get_json()
    if json_data:
        return login(json_data)


if __name__ == '__main__':
    createdb()
    app.run(debug=True, port=80)