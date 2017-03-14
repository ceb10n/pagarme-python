# encoding: utf-8

import mock

from .mocks import fake_get_bankAccount, fake_create_BankAccount
from pagarme.bankAccount import BankAccount
from .pagarme_test import PagarmeTestCase


class BankAccountTestCase(PagarmeTestCase):

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_bankAccount))
    def test_get_bankAccount_by_id(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_id(17422412)
        self.assertEqual(17422412, bankAccount.id)



    @mock.patch('requests.post', mock.Mock(side_effect=fake_create_BankAccount))
    def test_create_bankAccount(self):
    	bankAccount = BankAccount(api_key='apikey', bank_code='341', agencia='0932', agencia_dv='4', conta='58054', conta_dv='1',type='conta_corrente',document_number='26268738888',legal_name='BANK ACCOUNT PYTHON')
    	bankAccount.charge()
    	self.assertEqual('26268738888',bankAccount.document_number)