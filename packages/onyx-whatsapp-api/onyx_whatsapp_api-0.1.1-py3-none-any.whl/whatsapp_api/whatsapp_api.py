import requests

BASE_URL = 'https://onyxberry.com/services/wapi/api2'

class WhatsAppAPI:
    def __init__(self, your_id, api_key):
        self.your_id = your_id
        self.api_key = api_key

    def send_simple_text_message(self, number, message):
        url = f'{BASE_URL}/sendtext/{self.your_id}/{self.api_key}'
        data = {'number': number, 'message': message}

        response = requests.post(url, data=data)
        return response.json()

    def send_media_from_url(self, number, url, caption=''):
        url = f'{BASE_URL}/sendFromURL/{self.your_id}/{self.api_key}'
        data = {'number': number, 'url': url, 'caption': caption}

        response = requests.post(url, data=data)
        return response.json()

    def send_text_in_group(self, group_name, message):
        url = f'{BASE_URL}/sendTextInGroup/{self.your_id}/{self.api_key}'
        data = {'groupName': group_name, 'message': message}

        response = requests.post(url, data=data)
        return response.json()

    def send_media_from_url_in_group(self, group_name, url, caption=''):
        url = f'{BASE_URL}/sendFromURLInGroup/{self.your_id}/{self.api_key}'
        data = {'groupName': group_name, 'url': url, 'caption': caption}

        response = requests.post(url, data=data)
        return response.json()

# Optional: Include a main function for command-line usage
def main():
    your_id = 'your_id'
    api_key = 'your_api_key'

    whatsapp = WhatsAppAPI(your_id, api_key)

    # Example usage
    result = whatsapp.send_simple_text_message('recipient_number', 'Hello, this is a test message')
    print(result)

    result = whatsapp.send_media_from_url('recipient_number', 'media_url', 'Optional caption')
    print(result)

    result = whatsapp.send_text_in_group('group_name', 'Hello, this is a group message')
    print(result)

    result = whatsapp.send_media_from_url_in_group('group_name', 'media_url', 'Optional caption')
    print(result)

if __name__ == "__main__":
    main()
