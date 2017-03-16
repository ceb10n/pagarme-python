# encoding utf-8

import mock

from .mocks import fake_get_payable_by_id
from .pagarme_test import PagarmeTestCase
from pagarme.payable import Payable

class PayableTestCase(PagarmeTestCase):

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_payable_by_id))
    def test_get_payable_by_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_id(906983)
        self.assertEqual(906983, payable.id)