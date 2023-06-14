import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Authorization': token
        }
        params = {
            'path': 'Watermellon.jpeg'
        }
        response = requests.get(url, headers=headers, params=params)
        url_for_upload = response.json().get('href', '')
        with open(file_path, 'rb') as file:
            response2 = requests.put(url_for_upload, files={'file': file})

if __name__ == '__main__':
    path_to_file = 'Арбуз.jpeg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
