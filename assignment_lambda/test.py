""" basic test for GitHub CI process"""
import unittest
from main import basic_function, read_data, extract_analysis


class TestStringMethod(unittest.TestCase):
    """ basic test"""

    def test_basic_function_fails(self):
        """ fail test"""
        self.assertNotEqual(basic_function(), "")

    def test_basic_function_pass(self):
        """ pass test"""
        self.assertEqual(basic_function(), "hello world")

    def test_load_file(self):
        """ load file success"""
        test_dict = {"a": 1}
        self.assertDictEqual(read_data("unit_test_data.json"), test_dict)

    def test_load_file_fail(self):
        """ load file fail"""
        self.assertEqual(read_data("file_does_not_exist.json"),
                         "[Errno 2] No such file or directory: 'file_does_not_exist.json'")

    def test_extract_analysis(self):
        """ extract analysis success"""
        test_dict = {'employee_total': 3, 'courses': {
            'AWS Foundation', 'Go foundation'}}
        data = read_data('test_data.json')
        self.assertDictEqual(extract_analysis(data), test_dict)

    def test_extract_analysis_fails(self):
        """ extract analysis fail"""
        data = {"a": 1}
        self.assertEqual(extract_analysis(
            data), "'int' object is not subscriptable")


if __name__ == "__main__":
    unittest.main()
