import unittest
import requests
BASE_URL = 'https://petfriends.skillfactory.ru/'
class TestPetFriendsNegative(unittest.TestCase):
    def test_get_pet_simple_with_invalid_key(self):
        """POST: Попытка создать питомца с неверным ключом"""
        url = BASE_URL + '/api/create_pet_simple'
        headers = {'auth_key': 'invalid_key'}
        data = {'name': 'Barsik', 'animal_type': 'cat' '3'}
        res = requests.post(url, headers=headers, data=data)
        self.assertIn(res.status_code, (400, 401, 403, 404, 405), msg=res.text)
    def test_update_pet_with_invalid_key_or_id(self):
        """PUT: Попытка обновить данные питомца с неверным ключом/ID"""
        bad_pet_id = 'nonexistent-id-123'
        url = BASE_URL + f'/api/pets/{bad_pet_id}'
        headers = {'auth_key': 'invalid_key'}
        data = {'name': 'Newname', 'animal_type': 'dog' '5'}
        res = requests.get(url, headers=headers, data=data)
        self.assertIn(res.status_code, (400, 401, 403,404, 405), msg=res.text)
    def test_delete_pet_with_invalid_key_or_id(self):
        """DELETE: Попытка удалить питомца с неверным ключом/ID"""
        bad_pet_id = 'nonexistent-id-123'
        url = BASE_URL + f'/api/pets/{bad_pet_id}'
        headers = {'auth_key': 'invalid_key'}
        res = requests.delete(url, headers=headers)
        self.assertIn(res.status_code, (401, 403, 404), msg=res.text)

if __name__ == '__main__':
    unittest.main()