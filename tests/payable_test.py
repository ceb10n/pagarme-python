# encoding utf-8

import mock

from .mocks import fake_get_payable_by_id,fake_request_fail
from .pagarme_test import PagarmeTestCase
from pagarme.payable import Payable,PagarmeApiError

class PayableTestCase(PagarmeTestCase):

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_payable_by_id))
    def test_get_payable_by_id(self):
        payable = Payable(api_key='api_key')
        payable.find_by_id(906983)
        self.assertEqual(906983, payable.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail))
    def test_get_payable_by_id_fails(self):
        payable = Payable(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            payable.find_by_id(906983)