from Back.Utils import *

Builder.load_file("Front/screen_manager.kv")
Builder.load_file("Front/Home.kv")
Builder.load_file("Front/Cadastro.kv")
Builder.load_file("Front/Pesquisa.kv")
Builder.load_file("Front/Configuracoes.kv")
Builder.load_file("Front/Playlists.kv")
Builder.load_file("Front/Downloads.kv")

app = Flask(__name__)


class Podfy(MDApp):

    #Importação de Fontes
    inter_regular = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Regular.ttf')
    inter_medium = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Medium.ttf')
    inter_semibold = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-SemiBold.ttf')
    inter_bold = os.path.join(os.path.dirname('Back'), 'Front','resources', 'fontes', 'Inter', 'static', 'Inter-Bold.ttf')


    #Importação de imagens e ícones
    podfy_logo_white = os.path.join (os.path.dirname('Back'), 'Front','resources', 'podfy-logo-whitebg.jpg')
    podfy_mini_logo = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bar-podfy-logo.png')
    podfy_mini_logo_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bar-podfy-logo_hover.png')
    app_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','icon.png')
    
    user_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','profile_icon.png')
    user_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','profile_icon_hover.png')

    home_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','home.png')
    home_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','home-1.png')

    bars_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bars.png')
    bars_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','bars-1.png')

    search_icon = os.path.join(os.path.dirname('Back'), 'Front','resources','img','search.png')
    search_icon_hover = os.path.join(os.path.dirname('Back'), 'Front','resources','img','search-1.png')

    #Definição de Cores:
    color_yellow = '#FEC200' #Amarelo padrão Podfy
    color_gray ='#4F5357' # Cinza padrão Podfy
    bg_dark_default = '#121212' #Preto padrão para background
    bg_dark_lighter = '#252525' #Preto levemente mais claro para background
    

    def build(self):
        sm = WindowManager()
        sm.current = 'login_screen'
        # sm.current = 'home_screen' 


        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style = 'Dark'
        self.title = "Podfy"
        self.icon = self.app_icon
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


class WindowManager(ScreenManager):
    # Classe Root que vai lidar com transição de Screens
    pass

class ConfigScreen(Screen):
    pass

class CustomizeScreen(Screen):
    pass

class SearchScreen(Screen):
    pass

class PlaylistScreen(Screen):
    pass

class DownloadScreen(Screen):
    pass

class HomeScreen(Screen):
    pass


