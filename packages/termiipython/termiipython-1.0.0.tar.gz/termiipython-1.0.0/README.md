# termiipython

Termii Python Library for Termii API

## Installation

```bash
pip install termiipython
```

## Usage

- Send SMS

```bash
from termii.Termii import Termii

# Initialize a Termii instance with your sender ID and API key
termii = Termii(sender_id='TERMII_SENDER_ID', api_key='TERMII_API_KEY')

# Define the payload for sending an SMS
sms_payload = {
    'phone_number': 'RecipientPhoneNumber',
    'message': 'Hello, this is a test message from termiipython!'
    }

# Send the SMS
response = termii.send_message(sms_payload)

# Check the response
print(response)
```

- Send Token

```bash
from termii.Termii import Termii

# Initialize a Termii instance with your sender ID and API key
termii = Termii(sender_id='TERMII_SENDER_ID', api_key='TERMII_API_KEY')

# Define the payload for sending an SMS
sms_payload = {
    'phone_number': 'RecipientPhoneNumber',
    'message': 'Hello, this is a test message from termiipython!'
    }

# Send the SMS
response = termii.send_message(sms_payload)

# Check the response
print(response)
```

- Verify Token

```bash
from termii.Termii import Termii

# Initialize a Termii instance with your sender ID and API key
termii = Termii(sender_id='TERMII_SENDER_ID', api_key='TERMII_API_KEY')
verify_payload = {
    'pin_id': 'PinIdFromPreviousResponse',
    'pin': '123456'  # Replace with the actual PIN entered by the user
    }

# Verify the token
response = termii.verify_token(verify_payload)

# Check the verification response
print(response)
```

- InApp Token

```bash
from termii.Termii import Termii

# Initialize a Termii instance with your sender ID and API key
termii = Termii(sender_id='TERMII_SENDER_ID', api_key='TERMII_API_KEY')
# Define the payload for generating an in-app token
in_app_token_payload = {
    'phone_number': 'RecipientPhoneNumber',
    }

# Generate the in-app token
response = termii.in_app_token(in_app_token_payload)

# Check the in-app token response
print(response)
```

- Available Methods

```bash
from termii.Termii import Termii

# Initialize a Termii instance with your sender ID and API key
termii = Termii(sender_id='TERMII_SENDER_ID', api_key='TERMII_API_KEY')

termii.send_message()
termii.send_token()
termii.verify_token()
termii.in_app_token()
termii.send_with_auto_generated_number()
termii.get_sender_ids()
termii.get_response()
termii.set_max_attempts()
termii.set_pin_time_to_live()
termii.set_pin_type()
termii.set_channel()
termii.set_pin_placeholder()
termii.set_message_type()
termii.set_token_message_type()
termii.set_pin_length()
termii.set_sender()
termii.set_api_key()
termii.get_sender_ids()
termii.get_balance()
termii.search()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`termiipython` was created by Solomon Olatunji. It is licensed under the terms of the MIT license.
