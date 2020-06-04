import unittest
import requests


class TestYandexTranslate(unittest.TestCase):
    def setUp(self):
        self.API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {'key' : self.API_KEY, 'text' : 'hi', 'lang' : 'en-ru'}
        self.bad_direction = {'key' : self.API_KEY, 'text' : 'hi', 'lang' : 'en-rklm'}
        self.bad_key = {'key' : '88005553535', 'text' : 'hi', 'lang' : 'en-ru'}        

    def tearDown(self):
        pass

    def test_translation_text_and_code(self):
        response = requests.get(self.URL, params=self.params).json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['text'][0], 'привет')

    def test_negative_translation_direction(self):
        response = requests.get(self.URL, params=self.bad_direction).json()
        self.assertEqual(response['message'], 'The specified translation direction is not supported')

    def test_negative_bad_key(self):
        response = requests.get(self.URL, params=self.bad_key).json()
        self.assertEqual(response['message'], 'API key is invalid')


unittest.main()

