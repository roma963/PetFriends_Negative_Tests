import unittest
import requests
BASE_URL = 'https://petfriends.skillfactory.ru/'
class TestPetFriendsNegative(unittest.TestCase):
    def test_get_api_key_without_credentials(self):
        """Попробуем получить ключ без логина и пароля"""
        url = BASE_URL + 'apikey'
        headers = {}
        res = requests.get(url, headers=headers)
        self.assertIn(res.status_code, (403, 404), msg=res.text)
    def test_get_api_key_with_wrong_credentials(self):
        """попробуем получить ключ с неверным логином и паролем"""
        url = BASE_URL + 'apikey'
        headers = {'email': 'wrong@example.com', 'password': 'wrongpassword'}
        res = requests.get(url, headers=headers)
        self.assertIn(res.status_code, (403, 404), msg=res.text)
    def test_get_pets_with_invalid_key(self):
        """Попробуем запросить список питомцев с не правильным ключом"""
        url = BASE_URL + 'apikey'
        headers = {'auth_key': 'invalid_key'}
        res = requests.get(url, headers=headers)
        self.assertIn(res.status_code, (403, 404), msg=res.text)
if __name__ == '__main__':
    unittest.main()