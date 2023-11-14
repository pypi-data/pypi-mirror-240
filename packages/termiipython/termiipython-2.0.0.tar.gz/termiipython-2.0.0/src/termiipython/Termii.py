# Termii SMS APi Library for PHP
# Author: Solomon Olatunji
# Email: aotoluwalope@gmail.com

import requests
import json


class Termii:
    def __init__(self, sender_id='S-Alert', api_key=''):
        """
        Initializes the Termii class with default values for sender_id and api_key.
        """
        self.sender_id = sender_id
        self.api_key = api_key
        self.verify_ssl = True
        self.max_attempts = 3
        self.pin_time_to_live = 0
        self.pin_length = 6
        self.pin_placeholder = "< _pin_ >"
        self.pin_type = "NUMERIC"
        self.channel = "generic"
        self.token_message_type = "ALPHANUMERIC"
        self.message_type = "plain"
        self.response = None

    def send_message(self, payload):
        """
        Sends text messages to customers using the Termii API.
        For more information: http://developer.termii.com/docs/messaging/

        :param payload: Dictionary containing phone_number and message
        :return: Dictionary containing the API response
        """
        data = {
            "api_key": self.api_key,
            "from": self.sender_id,
            "channel": self.channel,
            "type": self.message_type,
            "to": payload['phone_number'],
            "sms": payload['message']
        }

        return self.post('sms/send', data)

    def send_token(self, payload):
        """
        Sends one-time-passwords (pins) across any available messaging channel on Termii.
        For more information: http://developer.termii.com/docs/send-token/

        :param payload: Dictionary containing phone_number and message
        :return: Dictionary containing the API response
        """
        data = {
            "api_key": self.api_key,
            "message_type": self.token_message_type,
            "to": payload['phone_number'],
            "from": self.sender_id,
            "channel": self.channel,
            "pin_attempts": self.max_attempts,
            "pin_time_to_live": self.pin_time_to_live,
            "pin_length": self.pin_length,
            "pin_placeholder": self.pin_placeholder,
            "message_text": payload['message'],
            "pin_type": self.pin_type
        }

        return self.post('sms/otp/send', data)

    def verify_token(self, payload):
        """
        Checks tokens sent to customers and returns a response confirming the status of the token.
        A token can either be confirmed as verified or expired based on the timer set for the token.
        For more information: http://developer.termii.com/docs/verify-token/

        :param payload: Dictionary containing the necessary information for token verification
        :return: Dictionary containing the API response payload
        """
        data = {
            "api_key": self.api_key,
            "pin_id": payload['pin_id'],
            "pin": payload['pin']
        }

        return self.post('sms/otp/verify', data)

    def in_app_token(self, payload):
        """
        Generates numeric or alpha-numeric codes (tokens) used to authenticate login requests and verify customer transactions.
        For more information: http://developer.termii.com/docs/in-app-token/

        :param payload: Dictionary containing the necessary information for in-app token generation
        :return: Dictionary containing the API response payload
        """
        data = {
            "api_key": self.api_key,
            "pin_type": self.pin_type,
            "phone_number": payload['phone_number'],
            "pin_attempts": self.max_attempts,
            "pin_time_to_live": self.pin_time_to_live,
            "pin_length": self.pin_length
        }

        return self.post('sms/otp/generate', data)

    def send_with_auto_generated_number(self, payload):
        """
        Sends messages to customers using Termii's auto-generated messaging numbers that adapt to customers' location.
        For more information: http://developer.termii.com/docs/number/

        :param payload: Dictionary containing the necessary information for sending a message with an auto-generated number
        :return: Dictionary containing the API response payload
        """
        data = {
            "api_key": self.api_key,
            "to": payload['phone_number'],
            "sms": payload['message']
        }

        return self.post('sms/number/send', data)

    def get_sender_ids(self):
        """
        Retrieves the status of all registered sender IDs and requests registration of a sender ID through a GET request.

        :return: Dictionary containing the API response payload
        """
        return self.get('sender-id', {"api_key": self.api_key})

    def post(self, path, payload):
        """
        Submits a POST request to Termii API.

        :param path: The API endpoint path
        :param payload: Dictionary containing the request payload
        :return: Dictionary containing the API response payload
        """
        response = requests.post(
            f'https://api.ng.termii.com/api/{path}',
            headers={'Content-Type': 'application/json'},
            json=payload,
            verify=self.verify_ssl
        )

        self.response = response
        r_dict = json.loads(response.text)
        return r_dict

    def get(self, path, payload):
        """
        Submits a GET request to Termii API.

        :param path: The API endpoint path
        :param payload: Dictionary containing the request payload
        :return: Dictionary containing the API response payload
        """
        response = requests.get(
            f'https://api.ng.termii.com/api/{path}',
            headers={'Content-Type': 'application/json'},
            params=payload,
            verify=self.verify_ssl
        )

        self.response = response
        r_dict = json.loads(response.text)
        return r_dict

    def get_response(self):
        """
        Gets the last response from Termii API.

        :return: API response object or None if no response is available
        """
        return self.response if self.response else None

    def set_max_attempts(self, attempts):
        """
        Sets the maximum number of attempts for PIN verification.

        :param attempts: The maximum number of attempts
        :return: Instance of the Termii class
        """
        self.max_attempts = attempts
        return self

    def set_pin_time_to_live(self, minute):
        """
        Sets the time-to-live (TTL) for the PIN in minutes.

        :param minute: The time-to-live in minutes
        :return: Instance of the Termii class
        """
        self.pin_time_to_live = minute
        return self

    def set_pin_type(self, pin_type):
        """
        Sets the type of PIN (e.g., NUMERIC, ALPHANUMERIC).

        :param pin_type: The type of PIN
        :return: Instance of the Termii class
        """
        self.pin_type = pin_type
        return self

    def set_channel(self, channel):
        """
        Sets the channel to send messages via (e.g., generic, dnd).

        :param channel: The messaging channel
        :return: Instance of the Termii class
        """
        self.channel = channel
        return self

    def set_pin_placeholder(self, placeholder):
        """
        Sets the placeholder for the PIN in the message.

        :param placeholder: The placeholder for the PIN
        :return: Instance of the Termii class
        """
        self.pin_placeholder = placeholder
        return self

    def set_message_type(self, message_type):
        """
        Sets the type of message (e.g., plain).

        :param message_type: The type of message
        :return: Instance of the Termii class
        """
        self.message_type = message_type
        return self

    def set_token_message_type(self, token_message_type):
        """
        Sets the type of token message (e.g., ALPHANUMERIC).

        :param token_message_type: The type of token message
        :return: Instance of the Termii class
        """
        self.token_message_type = token_message_type
        return self

    def set_pin_length(self, pin_length):
        """
        Sets the length of the PIN.

        :param pin_length: The length of the PIN
        :return: Instance of the Termii class
        """
        self.pin_length = pin_length
        return self

    def set_sender(self, sender):
        """
        Sets the sender ID.

        :param sender: The sender ID to be set
        :return: Instance of the Termii class
        """
        self.sender_id = sender
        return self

    def set_api_key(self, key):
        """
        Sets the API key.

        :param key: The API key to be set
        :return: Instance of the Termii class
        """
        self.api_key = key
        return self
