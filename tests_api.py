import os
import unittest
import requests
BASE_URL = 'https://petfriends.skillfactory.ru/'
class TestPetFriendsNegative(unittest.TestCase):
    def test_update_pet_with_valid_data(self):
        """PUT: Проверка, что данные питомца можно обновить с валидным ключом """
        url_create = BASE_URL + 'api/create_pet_simple'
        headers = {'auth_key': os.environ['PF_API_KEY']}
        data = {'name': 'TempPet', 'animal_type': 'dog', 'age': '1'}
        res = requests.post(url_create, headers=headers, data=data)
        self.assertEqual(res.status_code, 200, msg=res.text)
        pet_id = res.json()['id']
        url_update = BASE_URL + f'api/pets/{pet_id}'
        new_data = {'name': 'UpdatedPet', 'animal_type': 'cat', 'age': '3'}
        res = requests.put(url_update, headers=headers, data=new_data)
        self.assertEqual(res.status_code, 200, msg=res.text)
        body = res.json()
        self.assertEqual(body['name'], 'UpdatedPet')
        self.assertEqual(body['animal_type'], 'cat')
        self.assertEqual(body['age'], '3')


if __name__ == '__main__':
    unittest.main()

