# Termii SMS API Library for Python
# Author: Solomon Olatunji
# Email: aotoluwalope@gmail.com

from termiipython.Termii import Termii


class Insight(Termii):
    """
    Extends the Termii class to provide additional functionalities for retrieving insights and information.
    Inherits methods for sending messages and managing settings from the base Termii class.

    :param sender_id: Default sender ID for Insight class
    :param api_key: API key for authentication
    """

    def __init__(self, sender_id='S-Alert', api_key=''):
        super().__init__(sender_id, api_key)

    def get_sender_ids(self):
        """
        Retrieves reports for messages sent across the SMS, voice, and WhatsApp channels.

        :return: Dictionary containing the API response payload
        """
        return self.get('sms/inbox', self.payload())

    def get_balance(self):
        """
        Retrieves the total balance and balance information from the wallet, such as currency.

        :return: Dictionary containing the API response payload
        """
        return self.get('get-balance', self.payload())

    def search(self, phone_number):
        """
        Verifies phone numbers and automatically detects their status as well as the current network.
        It also tells if the number has activated the do-not-disturb settings.

        :param phone_number: Phone number to search for
        :return: Dictionary containing the API response payload
        """
        payload = {
            'api_key': self.api_key,
            'phone_number': phone_number
        }

        return self.get('check/dnd', payload)
