import unittest
import app
import json
from unittest.mock import patch

class TestDocumentAddRemoveSearch(unittest.TestCase):
    def setUp(self):
        self.doc_cat = []
        with open('fixture/docs.json') as f:
            self.doc_cat = json.load(f)
        self.dir_cat = []
        with open('fixture/dirs.json') as f:
            self.dir_cat = json.load(f)            

    def tearDown(self):
        pass

    def test_search_name_by_number(self):
        found = app.search_name_by_number(self.doc_cat, self.doc_cat[0]['number'])
        searched = self.doc_cat[0]['name']
        self.assertEqual(found, searched)

    def test_find_shelf(self):
        found = app.find_shelf(self.dir_cat['2'][1], self.dir_cat)
        searched = '2'
        self.assertEqual(found, searched)

    def test_add_doc(self):
        before_len = len(self.doc_cat)
        user_input = ['passport', '7555545', 'Vasya Pupkin', '2']
        with patch('app.input', side_effect=user_input):
            app.add_doc(self.doc_cat, self.dir_cat)
        after_len = len(self.doc_cat)
        self.assertLess(before_len, after_len)

    def test_delete_doc(self):
        before_len = len(self.doc_cat)
        user_input = [self.doc_cat[0]['number'], 'y']
        with patch('app.input', side_effect=user_input):
            app.delete_doc(self.doc_cat, self.dir_cat)
        after_len = len(self.doc_cat)
        self.assertGreater(before_len, after_len)




unittest.main()

