import  requests
BASE_URL = 'https://petfriends.skillfactory.ru/'

class PetFriends:
    def get_api_key(self, email: str,password: str) -> dict:
        """Получить API - ключдля указанной пары email/пароль."""
        url = BASE_URL + 'api/key'
        headers = {
                'email': email,
                'password': password
              }
        res = requests.get(url,headers=headers)
        status = res.status_code
        result = res.json()
        return status,  result
