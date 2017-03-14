# encoding: utf-8

import requests

from .exceptions import PagarmeApiError, NotPaidException, NotBoundException
from .resource import AbstractResource


class BankAccount(AbstractResource):
    BASE_URL = 'https://api.pagar.me/1/bank_accounts'

    def __init__(
        self,
        api_key=None,
        bank_code=None,
        agencia=None,
        agencia_dv=None,
        conta=None,
        conta_dv=1,
        type=['conta_corrente','conta_poupanca','conta_corrente_conjunta','conta_poupança_conjunta'],
        document_number=None,
        legal_name=None,
        **kwargs):

        self.api_key = api_key
        self.bank_code = bank_code
        self.agencia = agencia
        self.agencia_dv = agencia_dv
        self.conta = conta
        self.conta_dv = conta_dv
        self.type = type
        self.document_number = document_number
        self.legal_name = legal_name
        self.id = None
        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = value

    def charge(self):
    	self.create()

    def handle_response(self, data):
        self.id = data['id']
        self.bank_code = data['bank_code']
        self.agencia = data['agencia']
        self.agencia_dv = data['agencia_dv']
        self.conta = data['conta']
        self.conta_dv = data['conta_dv']
        self.type = data['type']
        self.document_number = data['document_number']
        self.legal_name = data['legal_name']
    
    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        d['bank_code'] = self.bank_code
        d['agencia'] = self.agencia
        d['agencia_dv'] = self.agencia_dv
        d['conta'] = self.conta
        d['conta_dv'] = self.conta_dv
        d['type'] = self.type
        d['document_number'] = self.document_number
        d['legal_name'] = self.legal_name

        return d

    def get_data(self):
        return self.__dict__()

    def find_by_id(self, id=None):
        url = self.BASE_URL + '/' + str(id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())