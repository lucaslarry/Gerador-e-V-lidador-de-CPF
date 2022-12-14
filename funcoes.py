from re import sub
from random import randint

class Validar_cpf:
    
    def __init__(self):
        pass
    
    def gerar_digitos(self):
        digitos_gerados = ''
        for i in range(9):
            digitos_gerados += str(randint(0,9))
        return digitos_gerados


    def gerar_cpf(self):
        cpf = Validar_cpf.gerar_digitos(self)
        cpf_gerado = Validar_cpf.cpf_nove_digitos(self,cpf) + Validar_cpf.primeiro_digito(self,cpf) + Validar_cpf.segundo_digito(self,cpf)
        return cpf_gerado


    def formatar_cpf(self,cpf):
       if cpf == cpf[0] * len(cpf):
            return '0'
       else:
            return sub(
                    r'[^0-9]',
                    '',
                    cpf
                )
    

    def cpf_nove_digitos(self,cpf):
        return Validar_cpf.formatar_cpf(self,cpf)[:9]
        

    def primeiro_digito(self,cpf):
        multiplicar = 10
        soma = 0
        
        for numero in Validar_cpf.cpf_nove_digitos(self,cpf):
            soma += int(numero) * multiplicar
            multiplicar -=1

        conta = (soma * 10) % 11

        if conta > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = conta

        return str(primeiro_digito)
    

    def segundo_digito(self,cpf):
        primeiro_digito = Validar_cpf.primeiro_digito(self,cpf)

        multiplicar = 11
        soma = 0

        for numero in Validar_cpf.cpf_nove_digitos(self,cpf) + primeiro_digito:
            soma += int(numero) * multiplicar
            multiplicar -= 1

        conta = (soma * 10) % 11

        if conta > 9:
            segundo_digito = 0
        else:
            segundo_digito = conta

        return str(segundo_digito)
    

    def validar_cpf(self,cpf):
        cpf_novo = Validar_cpf.cpf_nove_digitos(self,cpf) + Validar_cpf.primeiro_digito(self,cpf) + Validar_cpf.segundo_digito(self,cpf) 
        
        if cpf_novo == Validar_cpf.formatar_cpf(self,cpf):
            return True
        else:
            return False
    
    def formatar_string_novo_cpf(self,cpf):
        return f'Seu novo CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'