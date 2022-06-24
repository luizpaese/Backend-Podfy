from Back.Utils import *

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    email = ObjectProperty(None)
    confirm = ObjectProperty(None)
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)
    dataSelecionada = date.today() #Pega a data atual
    is_checkBox_active = False

    def btn(self):
        if Validar.validar_user(self.email.text, self.confirm.text, self.cpf.text, self.senha.text, self.dataSelecionada, self.is_checkBox_active):
            user = Validar.validar_user(self.email.text, self.confirm.text, self.cpf.text, self.senha.text, self.dataSelecionada, self.is_checkBox_active)
            print(user.cpf, user.email, user.senha)

    def on_save(self, instance, dataValue, date_range):
        self.dataSelecionada = dataValue #Atribui o valor da data para a variável "dataSelecionada"
        print(instance, dataValue, date_range) #vai printar a instancia, a data no formato (AAAA-MM-DD), e um intervalo de datas, caso houvesse
    
    def on_cancel(self, instance, value):
        pass

    #seletor de data KivyMD
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()


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
        Validar.error_message(3)
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
        if not email:
            print('Por favor informe um email.')
            Validar.error_message(0)
            return False

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.][a-z]{2,3})+$'
        if not re.search(regex, email):
            print('Email inválido')
            Validar.error_message(1)
            return False

        elif email == confirm:
            return True
        Validar.error_message(2)
        print('Confirmação de email não confere com o email informado')
        return False

    def validar_senha(senha):
        if len(senha) < 8:
            Validar.error_message(4)
            print('Informe uma senha de no minimo 8 digitos')
            return False
        elif not re.search('[a-zA-Z]', senha):
            Validar.error_message(4)
            print('Informe pelo menos uma letra maiuscula e minuscula (A-Z e a-z)')
            return False

        elif not re.search('[A-Z]', senha):
            Validar.error_message(4)
            print('Informe pelo menos uma letra maiuscula(A-Z)')
            return False
        elif not re.search('[a-z]', senha):
            Validar.error_message(4)
            print('Informe pelo menos uma letra minuscula(a-z)')
            return False
        return True

    def validar_data(dataSelecionada):
        today = date.today() #Pega a data atual
        age = today.year - dataSelecionada.year - ((today.month, today.day) < (dataSelecionada.month, dataSelecionada.day))

        if (dataSelecionada == today): #Caso a data selecionada seja igual a data atual, é porque o usuário não selecionou nenhuma data!
            print ("A data de Nascimento é obrigatória")
            Validar.error_message(5)
            return False
        elif (age < 18):
            print ("Idade inválida")
            Validar.error_message(6)
            return False
        return True

    def isCheckBoxActive (checkbox_active):
        
        if checkbox_active == False:
            print ("A checkbox não foi marcada!")
            Validar.error_message(7)
            return False
        return True

    def validar_user(email: str, confirm: str, cpf, senha: str, dataSelecionada, is_checkBox_active) -> bool or User:

        if not Validar.validar_email(email, confirm):
            return False

        if not Validar.validar_CPF(cpf):
            return False

        if not Validar.validar_senha(senha):
            return False

        if not Validar.validar_data(dataSelecionada):
            return False

        if not Validar.isCheckBoxActive(is_checkBox_active):
            return False

        cpf = Validar.validar_CPF(cpf)
        user = User(email, cpf, senha)
        print('Cadastro realizado com sucesso!')
        dialog = MDDialog(text = "Cadastro Realizado com Sucesso!")
        dialog.open()
        return user

    def error_message(error_type: int):

        # Error types:

        # 0 - Nenhum email informado
        # 1 - Email no formato invalido
        # 2 - Confirmacao diferente do email
        # 3 - CPF invalido
        # 4 - Senha Invalida
        # 5 - Nenhuma data Selecionada
        # 6 - Idade invalida (Menor que 18)
        # 7 - Checkbox nao foi marcada

        if (error_type == 0):
            dialog = MDDialog(text = "Nenhum email foi informado")
            dialog.open()
        elif (error_type == 1):
            dialog = MDDialog(text = "O email deve ter o formato: exemplo@exemplo.com")
            dialog.open()
        elif (error_type == 2):
            dialog = MDDialog(text = "A confirmação deve ser igual ao email fornecido")
            dialog.open()
        elif (error_type == 3):
            dialog = MDDialog(text = "CPF inválido")
            dialog.open()
        elif (error_type == 4):
            dialog = MDDialog(text = "A senha deve conter no mínimo 8 dígitos, incluindo letras maísculas e minúsculas")
            dialog.open()
        elif (error_type == 5):
            dialog = MDDialog(text = "Nenhuma data de nascimento foi selecionada")
            dialog.open()
        elif (error_type == 6):
            dialog = MDDialog(text = "A data de nascimento é inválida")
            dialog.open()
        elif (error_type == 7):
            dialog = MDDialog(text = "A caixa de seleção não foi marcada")
            dialog.open()


    
