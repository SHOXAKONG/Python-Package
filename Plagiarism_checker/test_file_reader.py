import unittest
from file_reader import read_file

class TestFileReader(unittest.TestCase):
    def test_read_docx(self):
        text = read_file("sample.docx")
        self.assertIn("Expected text", text)

    def test_read_pdf(self):
        text = read_file("sample.pdf")
        self.assertIn("Expected text", text)

    def test_read_text_file(self):
        text = read_file("sample.txt")
        self.assertIn("Expected text", text)

    def test_unsupported_file_type(self):
        with self.assertRaises(ValueError):
            read_file("sample.xlsx")
