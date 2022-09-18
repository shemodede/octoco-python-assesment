import unittest
import naughty_pup

class CreateTestResourceTextFiles:
    def __init__(self):
        self.txt_test_file_name = "test_file.txt"
        self.csv_test_file_name = "test_file.csv"
        self.md_test_file_name = "test_file.md"

class TestNaughtyPup(unittest.TestCase):
    def test_troll_check(self):
        pass

    def test_print_troll_checked(self):
        pass

    def test_scan_directory(self):
        num_of_troll_files = naughty_pup.scan_directory("directory")
        expected_result = 2
        self.assertEquals(num_of_troll_files, expected_result)
