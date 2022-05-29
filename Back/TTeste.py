import re

class Validar:

    def validar_CPF(self, cpf) -> ():
        Num_CPF = re.sub('[^0-9]', '', cpf)
        sequencia = cpf[0] * len(cpf)
        print(sequencia)
        return Num_CPF

if __name__ == '__main__':
    cpf1 = '256.630.970-15'
    Validar.validar_CPF(cpf1)