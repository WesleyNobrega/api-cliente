import re
from validate_docbr import CPF



def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(cpf.mask(numero_do_cpf))
def nome_valido(nome):
    return nome.isalpha()
def rg_valido(rg):
    return len(rg) == 9
def telefone_valido(telefone):
    """ Verifica se o número de telefone é válido (99 99999-9999)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,telefone)
    return resposta