from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import re


class RegisterScreen(Screen):
    email = ObjectProperty(None)
    confirm = ObjectProperty(None)
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)

    def btn(self):
        Validar.validar_user(self.email.text, self.email.text, self.confirm.text, self.cpf.text, self.senha.text)



class User:
    def __init__(self, email, cpf, senha):
        self.email = email
        self.cpf = cpf
        self.senha = senha


class Validar:

    def validar_CPF(cpf: str) -> bool or str:
        cpf = re.sub('\D', '', cpf)
        fatia_CPF = cpf[:9]
        novo_CPF = Validar.calcula_dig(fatia_CPF)
        novo_CPF = Validar.calcula_dig(novo_CPF)

        if novo_CPF == cpf:
            return cpf
        print('CPF inválido')
        return False

    @staticmethod
    def calcula_dig(fatia_CPF) -> ():
        if not fatia_CPF:
            return False

        sequencia = fatia_CPF[0] * len(fatia_CPF)

        if sequencia == fatia_CPF:
            return False

        soma = 0
        for chave, mult in enumerate(range(len(fatia_CPF) + 1, 1, -1)):
            soma += int(fatia_CPF[chave]) * mult

        resto = 11 - (soma % 11)
        resto = resto if resto <= 9 else 0
        return fatia_CPF + str(resto)

    # 413.717.708-24

    def validar_email(email, confirm):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w{2,3})+$'
        if not re.search(regex, email):
            print('Email inválido')
            return False

        elif email == confirm:
            return True
        print('Confirmação de email não confere com o email informado')
        return False

    def validar_senha(senha):
        if len(senha) < 12:
            print('Informe uma senha de no minimo 12 digitos')
            return False
        elif not re.search('[a-zA-Z]', senha):
            print('Informe pelo menos uma letra maiuscula e minuscula (A-Z e a-z)')
            return False

        elif not re.search('[A-Z]', senha):
            print('Informe pelo menos uma letra maiuscula(A-Z)')
            return False
        elif not re.search('[a-z]', senha):
            print('Informe pelo menos uma letra minuscula(a-z)')
            return False

        return True

    def validar_user(self, email: str, confirm: str, cpf, senha: str) -> bool or User:

        if not Validar.validar_email(email, confirm):
            return False

        if not Validar.validar_CPF(cpf):
            return False

        if not Validar.validar_senha(senha):
            return False

        cpf = Validar.validar_CPF(cpf)
        user = User(email, cpf, senha)
        print('Cadastro realizado com sucesso!')
        return user
