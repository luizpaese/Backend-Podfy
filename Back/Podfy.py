from Back.Utils import *


GUI = Builder.load_file("Front/Cadastro.kv")
GUI = Builder.load_file("Front/screen_manager.kv")
GUI = Builder.load_file("Front/Customizacao.kv")



# importações BD
from flask import Flask, request as flask_request
import sqlite3 as sql
import os

# importações crypt
import Back.Crypt


app = Flask(__name__)


class Podfy(App):

    #Importação de Fontes
    inter_regular = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Regular.ttf')
    inter_medium = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Medium.ttf')
    inter_semibold = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-SemiBold.ttf')
    inter_bold = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Bold.ttf')


    #Importação de imagens e ícones
    podfy_logo_white = os.path.join (os.path.dirname('Back'), 'Front','resources', 'podfy-logo-whitebg.jpg')
    podfy_mini_logo = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bar-podfy-logo.png')
    
    user_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','profile_icon.png')
    user_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','profile_icon_hover.png')

    home_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','home.png')
    home_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','home-1.png')

    bars_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bars.png')
    bars_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bars-1.png')

    search_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','search.png')
    search_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','search-1.png')

    def build(self):
        sm = WindowManager()
        sm.current = 'customize_screen' #Tela padrão que o WindowManager vai iniciar
        return sm

    def users(json_data):
        password = Back.Crypt.encrypt(json_data["pass"])
        passw = password.decode('utf-8')
        print(passw)

        try:
            conn = sql.connect('database.db')
            cur = conn.cursor()
            cur.execute(f'INSERT INTO users (name, email, CPF, password) VALUES ("{json_data["name"]}", "{json_data["email"]}", "{json_data["cpf"]}", "{password}")')
            conn.commit()

            return f'Usuário: {json_data["name"]} inserido com o emails: {json_data["email"]}, cpf: {json_data["cpf"]} e senha: password: {password}'

        except Exception as e:
            return(str(e))

def createdb():
    if not os.path.exists('database.db'):
        conn = sql.connect('database.db')
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
        return Back.Cadastro.users(json_data)

    #if __name__ == '__main__':
    #    createdb()
    #    app.run(debug=True, port=80)



Window.size = (360, 800)

class WindowManager(ScreenManager):
    # Classe Root que vai lidar com transição de Screens
    pass

# ADICIONAR RECONHECIMENTO DE LOGIN VÁLIDO COMO FOI FEITO NA CLASSE "RegisterScreen(Screen)"
class LoginScreen(Screen):
    pass

class CustomizeScreen(Screen):
    pass
