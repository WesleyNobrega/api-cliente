from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido !"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números no campo NOME !"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 11 dígitos !"})
        if not telefone_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número do celular deve ser o modelo: 86 99999-9999 !"})
        return data
    