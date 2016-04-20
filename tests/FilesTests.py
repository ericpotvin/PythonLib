""" This script tests the basic crypt for an number.
"""

import unittest
import sys
from Files import Files

sys.path.insert(0, '..')

# Set the default tests path
TEST_PATH = "/tmp/test/"


class BaseCryptTests(unittest.TestCase):
    """
    Tests for `BaseCrypt.py`.
    """

    def test_get_file_list(self):
        """ Test get_file_list()
        """

        Files.write("empty", "file1.txt", TEST_PATH)
        Files.write("empty", "file2.txt", TEST_PATH)

        file_list = Files.get_file_list(TEST_PATH)

        self.assertTrue(len(file_list) == 2)
        self.assertTrue(file_list[1] == "file2.txt")

        Files.delete_files(TEST_PATH + "file1.txt")
        Files.delete_files(TEST_PATH + "file2.txt")

    def test_file_exists(self):
        """ Test file_exists()
        """

        Files.write("empty", "file1.txt", TEST_PATH)
        self.assertTrue(Files.file_exists(TEST_PATH + "file1.txt"))
        Files.delete_files(TEST_PATH + "file1.txt")

    def test_delete_files(self):
        """ Test delete_files()
        """

        Files.write("empty", "file1.txt", TEST_PATH)
        self.assertTrue(Files.file_exists(TEST_PATH + "file1.txt"))
        Files.delete_files(TEST_PATH + "file1.txt")
        self.assertFalse(Files.file_exists(TEST_PATH + "file1.txt"))

    def test_get_raw_contents(self):
        """ Test get_raw_contents()
        """

        Files.write("some content", "file1.txt", TEST_PATH)
        content = Files.get_raw_contents(TEST_PATH + "file1.txt")
        self.assertTrue(content == "some content")
        Files.delete_files(TEST_PATH + "file1.txt")

    def test_can_exclude_file(self):
        """ Test can_include_file()
        """

        Files.write("some content", "file1.txt", TEST_PATH)
        file_list = Files.get_file_list(TEST_PATH, ["file1.txt"])
        self.assertTrue(len(file_list) == 0)
        Files.delete_files(TEST_PATH + "file1.txt")

    def test_write_binary(self):
        """ Test can_include_file()
        """
        Files.write_binary("test", "binary.bin", TEST_PATH)
        self.assertTrue(Files.file_exists(TEST_PATH + "binary.bin"))
        content = Files.get_raw_contents(TEST_PATH + "binary.bin")
        self.assertTrue(content == "74657374")
        Files.delete_files(TEST_PATH + "binary.bin")

    def test_read_binary(self):
        """ Test can_include_file()
        """
        Files.write_binary("test", "binary.bin", TEST_PATH)
        content = Files.read_binary_file(TEST_PATH + "binary.bin", 0, 8)
        self.assertTrue(content == "test")


if __name__ == '__main__':
    unittest.main()
