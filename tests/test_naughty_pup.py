import unittest
from unittest import result
from .test_data.test_data import TROLL_CHECK_EXCEPTION_NEITHER_STRING, TROLL_CHECK_EXCEPTION_NILBOG_STRING, TROLL_CHECK_EXCEPTION_TROLL_STRING, TROLL_CHECK_WORD_REPLACEMENT_STRING
import question_3
import os


class CreateTestResourceTextFiles:
    def __init__(self):
        # troll check file names
        self.troll_check_text_replace_file_name = "troll_check_word_replacement.txt"
        self.troll_check_with_troll_exception_test_file_name = "troll_check_with_troll_exception_text_file.txt"
        self.troll_check_with_nilbog_exception_test_file_name = "troll_check_with_nilbog_exception_text_file.txt"
        self.troll_check_with_neither_exception_test_file_name = "troll_check_with_neither_exception_text_file.txt"

        # scan directory file names
        self.scan_directory_txt_test_file_name = "scan_directory_text_file.txt"
        self.scan_directory_csv_test_file_name = "scan_directory_csv_file.csv"
        self.scan_directory_md_test_file_name = "scan_directory_md_file.md"

    def createWordReplacementFile(self):
        with open(self.troll_check_text_replace_file_name, "w") as f:
            f.write(TROLL_CHECK_WORD_REPLACEMENT_STRING)

    def createTrollExceptionFile(self):
        with open(self.troll_check_with_troll_exception_test_file_name, "w") as f:
            f.write(TROLL_CHECK_EXCEPTION_TROLL_STRING)

    def createNilbogExceptionFile(self):
        with open(self.troll_check_with_nilbog_exception_test_file_name, "w") as f:
            f.write(TROLL_CHECK_EXCEPTION_NILBOG_STRING)

    def createTrollCheckNeitherExceptionFile(self):
        with open(self.troll_check_with_neither_exception_test_file_name, "w") as f:
            f.write(TROLL_CHECK_EXCEPTION_NEITHER_STRING)

    def deleteTrollCheckFunctionFiles(self):
        os.remove(self.troll_check_text_replace_file_name)
        os.remove(self.troll_check_with_troll_exception_test_file_name)
        os.remove(self.troll_check_with_nilbog_exception_test_file_name)
        os.remove(self.troll_check_with_neither_exception_test_file_name)


class TestTrollCheckFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.resource_class = CreateTestResourceTextFiles()
        self.resource_class.createWordReplacementFile()
        self.resource_class.createTrollExceptionFile()
        self.resource_class.createNilbogExceptionFile()
        self.resource_class.createTrollCheckNeitherExceptionFile()
        return super().setUp()

    def tearDown(self) -> None:
        self.resource_class.deleteTrollCheckFunctionFiles()
        return super().tearDown()

    def test_troll_check_word_replacement(self):
        file = open(self.resource_class.troll_check_text_replace_file_name)
        text = file.read()
        file.close()
        # check if the words `goblin` and `hobgoblin` are in the text.
        self.assertTrue("goblin" in text)
        self.assertTrue("hobgoblin" in text)
        # call troll_check function
        resp_text = question_3.troll_check(text)
        # check if the words `goblin` and `hobgoblin` are not in returned text.
        self.assertFalse("goblin" in resp_text)
        self.assertFalse("hobgoblin" in resp_text)
        # Check if the words `elf` and `orc` are in returned text.
        self.assertTrue("elf" in resp_text)
        self.assertTrue("orc" in resp_text)

    def test_troll_check_troll_exception_raised(self):
        file = open(self.resource_class.troll_check_with_troll_exception_test_file_name)
        text = file.read()
        file.close()
        # check if the word `troll` is in the text
        self.assertTrue("troll" in text)
        # test exception raise after troll_check function call
        self.assertRaises(question_3.TheyreEatingHer, question_3.troll_check, text)


    def test_troll_check_nilbog_exception_raised(self):
        file = open(self.resource_class.troll_check_with_nilbog_exception_test_file_name)
        text = file.read()
        file.close()
        # check if the word `nilbog` is in the text
        self.assertTrue("nilbog" in text.lower())
        # check if the word `troll` is not found in text
        self.assertTrue("troll" not in text.lower())
        # test exception raise after troll_check function call
        self.assertRaises(question_3.ThenTheyreGoingToEatMe, question_3.troll_check, text)

    def test_troll_check_neither_exception_raised(self):
        file = open(self.resource_class.troll_check_with_neither_exception_test_file_name)
        text = file.read()
        file.close()
        # check if the word `nilbog` is not in the text
        self.assertTrue("nilbog" not in text.lower())
        # check if the word `troll` is not found in text
        self.assertTrue("troll" not in text.lower())
        # test exception raise after troll_check function call
        resp_text = question_3.troll_check(text)
        self.assertEqual(resp_text.lower(), text.lower())


class TestPrintTrollCheckFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.resource_class = CreateTestResourceTextFiles()
        self.resource_class.createWordReplacementFile()
        self.resource_class.createTrollExceptionFile()
        self.resource_class.createNilbogExceptionFile()
        self.resource_class.createTrollCheckNeitherExceptionFile()
        return super().setUp()

    def tearDown(self) -> None:
        self.resource_class.deleteTrollCheckFunctionFiles()
        return super().tearDown()

    def test_neither_troll_nor_nilbog_result(self):
        result = question_3.print_troll_checked(self.resource_class.troll_check_with_neither_exception_test_file_name)
        self.assertEqual(result, 0)

    def test_with_troll_in_file(self):
        result = question_3.print_troll_checked(self.resource_class.troll_check_with_troll_exception_test_file_name)
        self.assertEqual(result, 1)

    def test_with_nilbog_only_in_file(self):
        result = question_3.print_troll_checked(self.resource_class.troll_check_with_nilbog_exception_test_file_name)
        self.assertEqual(result, -1)

class TestScanDirectoryFunction(unittest.TestCase):

    def test_scan_directory(self):
        file_path = "tests/directory"
        num_of_troll_files = question_3.scan_directory(file_path)
        expected_result = 2
        self.assertEqual(num_of_troll_files, expected_result)
