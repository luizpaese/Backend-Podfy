from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

GUI = Builder.load_file("cadastro.kv")


class User:
    def __init__(self, email, cpf, senha):
        self.email = email
        self.cpf = cpf
        self.senha = senha


class MyGrid(Widget):
    email = ObjectProperty(None)
    confirm = ObjectProperty(None)
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)

    def btn(self):
        user = None

        if self.email.text == self.confirm.text and len(self.cpf.text) == 11:
            user = User(self.email.text, self.cpf.text, self.senha.text)
            App.get_running_app().stop()
            return user

        elif self.email.text != self.confirm.text or len(self.email.text) == 0:
            print("Email incorreto!")

        elif len(self.cpf.text) != 11:
            print("CPF inválido")



    def val(self):
            if self.email.text == self.confirm.text and len(self.cpf.text) == 11:
                user = User(self.email.text, self.cpf.text, self.senha.text)
                return user

            elif self.email.text != self.confirm.text or len(self.email.text) == 0:
                print("Email incorreto!")

            elif len(self.cpf.text) != 11:
                print("CPF inválido")




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
