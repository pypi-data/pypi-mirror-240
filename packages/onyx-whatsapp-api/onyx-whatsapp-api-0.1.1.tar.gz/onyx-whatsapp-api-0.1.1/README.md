# WhatsApp API Python Module

[![PyPI version](https://badge.fury.io/py/whatsapp-api.svg)](https://badge.fury.io/py/whatsapp-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whatsapp-api)
![PyPI - License](https://img.shields.io/pypi/l/whatsapp-api)

A Python module for sending WhatsApp messages using a third-party API.

## Installation

Install the module using pip:

```bash
pip install whatsapp-api

```


## Usage

from whatsapp_api import WhatsAppAPI

# Example usage
```bash
your_id = 'your_id'
api_key = 'your_api_key'

whatsapp = WhatsAppAPI(your_id, api_key)

# Sending a simple text message
result = whatsapp.send_simple_text_message('recipient_number', 'Hello, this is a test message')
print(result)

# Sending media from URL
result = whatsapp.send_media_from_url('recipient_number', 'media_url', 'Optional caption')
print(result)

# Sending text in a group
result = whatsapp.send_text_in_group('group_name', 'Hello, this is a group message')
print(result)

# Sending media in a group from URL
result = whatsapp.send_media_from_url_in_group('group_name', 'media_url', 'Optional caption')
print(result)
```

API Methods
send_simple_text_message(number, message)
Send a simple text message to the specified number.

number: Recipient's phone number.
message: Text message to be sent.
send_media_from_url(number, url, caption='')
Send images/PDF/documents, etc., from a URL to the specified number.

number: Recipient's phone number.
url: URL of the media file.
caption (Optional): Caption for the media file.
send_text_in_group(group_name, message)
Send a text message to a WhatsApp group.

group_name: Name of the WhatsApp group.
message: Text message to be sent.
send_media_from_url_in_group(group_name, url, caption='')
Send images/PDF/documents, etc., from a URL to a WhatsApp group.

group_name: Name of the WhatsApp group.
url: URL of the media file.
caption (Optional): Caption for the media file.
License
This project is licensed under the MIT License - see the LICENSE file for details.