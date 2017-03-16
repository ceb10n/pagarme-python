# encoding: utf-8

import requests

from .exceptions import PagarmeApiError, NotBoundException
from .resource import AbstractResource
from .settings import BASE_URL

class Payable(AbstractResource):
    BASE_URL = BASE_URL + 'payables'

    def __init__(self, 
        api_key=None,
        id=None, 
        status=None, 
        amount=None,
        fee=None, 
        installment=None,
        transaction_id=None, 
    	split_rule_id=None, 
        payment_date=None, 
        type=None, 
        date_created=None, 
        **kwargs):
        
        self.api_key = api_key
        self.id = id
        self.status = status
        self.amount = amount
        self.fee = fee
        self.installment = installment
        self.transaction_id = transaction_id
        self.split_rule_id = split_rule_id
        self.payment_date = payment_date
        self.type = type
        self.date_created = date_created
        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = value

    def handle_response(self,data):
        self.id = data['id']
        self.status = data['status']
        self.amount = data['amount']
        self.fee = data['fee']
        self.installment = data['installment']
        self.transaction_id = data['transaction_id']
        self.split_rule_id = data['split_rule_id']
        self.payment_date = data['payment_date']
        self.type = data['type']
        self.date_created = ['date_created']
        self.data = data

    def get_data(self):
        return self.__dict__()

    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        d['status'] = self.status
        d['amount'] = self.amount
        d['fee'] = self.fee
        d['installment'] = self.installment
        d['transaction_id'] = self.transaction_id
        d['split_rule_id'] = self.split_rule_id
        d['payment_date'] = self.payment_date
        d['type'] = self.type
        d['date_created'] = self.date_created

        return d

    def find_by_id(self, id):
        url = self.BASE_URL + '/' + str(id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())