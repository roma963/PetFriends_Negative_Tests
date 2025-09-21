import os
import unittest
import requests
BASE_URL = 'https://petfriends.skillfactory.ru/'
class TestPetFriendsNegative(unittest.TestCase):
    def test_get_pets_simple_with_valid_key(self):
        """GET: Проверка: что с действительным ключом список питомцев возвращается (200)"""
        url = BASE_URL + '/api/pets'
        headers = {'auth_key': os.environ['PF_API_KEY']}
        res = requests.get(url, headers=headers)
        self.assertEqual(res.status_code, 200, msg=res.text)
    def test_get_pets_valid_key(self):
        """GET: Проверка: получение списка питомцев с валидным ключом"""
        url = BASE_URL + '/api/pets'
        headers = {'auth_key': os.environ['PF_API_KEY']}
        res = requests.get(url, headers=headers)
        self.assertEqual(res.status_code, 200, msg=res.text)
        data = res.json()
        self.assertIn('pets', data, msg="В ответе нет ключа 'pets'")
        self.assertIsInstance(data['pets'],list, msg="Поле 'pets' должно быть списком")
    def test_add_new_pet_with_valid_data(self):
        """POST: Проверка: создание нового питомца с корректными данными"""
        url = BASE_URL + '/api/create_pet_simple'
        headers = {'auth_key': os.environ['PF_API_KEY']}
        data = {'name': 'bob', 'animal_type': 'German Shepherd', 'age': '2'}
        res = requests.post(url, headers=headers, data=data)
        self.assertEqual(res.status_code, 200, msg=res.text)
        body = res.json()
        self.assertEqual(body['name'], 'bob')
        self.assertEqual(body['animal_type'], "German Shepherd")
        self.assertEqual(body['age'], '2')
if __name__ == '__main__':
    unittest.main()

