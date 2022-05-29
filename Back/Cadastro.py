from Back.Imports import Builder, Widget, ObjectProperty, App

import re

GUI = Builder.load_file("Front/Cadastro.kv")


class MyGrid(Widget):
    email = ObjectProperty(None)
    confirm = ObjectProperty(None)
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)

    def btn(self):
        Validar.validar_user(self.email.text, self.email.text, self.confirm.text, self.cpf.text, self.senha.text)
        if self.email.text == self.confirm.text and len(self.cpf.text) == 11:
            user = User(self.email.text, self.cpf.text, self.senha.text)
            App.get_running_app().stop()
            return user

        elif self.email.text != self.confirm.text or len(self.email.text) == 0:
            print("Email incorreto!")

        elif len(self.cpf.text) != 11:
            print("CPF inválido")


class MyApp(App):
    def build(self):
        return MyGrid()


class User:
    def __init__(self, email, cpf, senha):
        self.email = email
        self.cpf = cpf
        self.senha = senha


class Validar:

    def validar_CPF(self, cpf) -> ():
        Num_CPF = re.sub('[^0-9]', '', cpf)
        sequencia = cpf[0] * len(cpf)
        print(sequencia)
        return Num_CPF

    def validar_email(self, email, confirm):
        pass

    def validar_user(self, email: str, confirm: str, cpf, senha: str) -> User:
        print('AAAAAA')

        num = self.validar_CPF('256.630.970-15')

        user = User(email, cpf, senha)
        return user
