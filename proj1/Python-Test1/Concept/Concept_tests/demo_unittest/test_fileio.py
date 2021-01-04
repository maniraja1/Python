import unittest
from unittest.mock import mock_open, patch
import json
import fileio

class TestFileIO(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,read_data=json.dumps({'name': 'John', 'shares': 100,
                                                                         'price': 1230.23}))
    def test_processfile(self,mock_file):
        expected_output = {
            'name': 'John',
            'shares': 100,
            'price': 1230.23
        }
        filename = 'example.json'
        actual_output = fileio.processfile(filename)

        # Assert filename is file that is opened
        mock_file.assert_called_with(filename, mode='r')

        self.assertEqual(expected_output, actual_output)

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({'name': 'John', 'shares': 100,
                                                                          'price': 1230.23}))
    def test_writefile(self, mock_file2):
        expected_output = {
            'name': 'John',
            'shares': 100,
            'price': 1230.23
        }
        filename = 'example.json'

        # Call function that writes
        fileio.writefile(filename)

        # Assert filename is file that is opened
        mock_file2.assert_called_with(filename, mode='w')

        # Create a file handler
        handle = mock_file2()

        # Assert File content
        handle.write.assert_any_call(expected_output)



if __name__ == '__main__':
    unittest.main()