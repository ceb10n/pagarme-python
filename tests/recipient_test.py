# encoding: utf-8

import mock

from .mocks import fake_get_recipient, fake_create_recipient
from pagarme.recipient import Recipient
from pagarme.bankAccount import BankAccount
from .pagarme_test import PagarmeTestCase


class RecipientTestCase(PagarmeTestCase):

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_recipient))
    def test_get_recipient_by_id(self):
        recipient = Recipient(api_key='apikey')
        recipient.find_by_id('re_cj01ath3700xqs56dmv00epj6')
        self.assertEqual('re_cj01ath3700xqs56dmv00epj6', recipient.id)

    @mock.patch('requests.post', mock.Mock(side_effect=fake_create_recipient))
    def test_create_recipient(self):

    	bank_Account = BankAccount(bank_code='341', agencia='0932', agencia_dv='4', conta='58054', conta_dv='1',
    		type='conta_corrente',document_number='26268738888',legal_name='BANK ACCOUNT PYTHON')

    	recipient = Recipient(api_key='apikey', transfer_interval='weekly', transfer_day='5', transfer_enabled='true', 
    		automatic_anticipation_enabled='true', anticipatable_volume_percentage='85', bank_account=bank_Account)

    	recipient.charge()
    	self.assertEqual('re_cj01ath3700xqs56dmv00epj6',recipient.id)