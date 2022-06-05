import sys
sys.path.append('../')
from client import create_presence, process_ans
from common.variables import *
import unittest
from errors import ReqFieldMissingError, ServerError


class TestClass(unittest.TestCase):
    def test_def_presence(self):
        test = create_presence('Guest')
        test[time_var] = 1.1
        self.assertEqual(test, {action: presence, time_var: 1.1, user: {acc_name: 'Guest'}})

    def test_200_ans(self):
        self.assertEqual(process_ans({response: 200}), '200 : OK')

    def test_400_ans(self):
        self.assertRaises(ServerError, process_ans, {response: 400, error: 'Bad Request'})

    def test_no_response(self):
        self.assertRaises(ReqFieldMissingError, process_ans, {error: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
