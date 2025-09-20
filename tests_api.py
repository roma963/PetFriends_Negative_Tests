import unittest
import requests
BASE_URL = 'https://petfriends.skillfactory.ru/'
class TestPetFriendsNegative(unittest.TestCase):
    def test_get_pets_wihut_key(self):
        url = BASE_URL + '/api/pets'
        res = requests.get(url)
        self.assertIn(res.status_code, (401, 403), msg=res.text)
    def test_get_pets_with_invalid_key(self):
        url = BASE_URL + '/api/pets'
        headers = {'auth_key': 'invalid_key'}
        res = requests.get(url, headers=headers)
        self.assertIn(res.status_code, (401, 403), msg=res.text)

if __name__ == '__main__':
    unittest.main()