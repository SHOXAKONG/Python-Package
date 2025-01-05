import os
from Plagiarism_checker.checker import PlagiarismChecker
from Plagiarism_checker.file_reader import read_file
from Plagiarism_checker import utils

utils.setup_logging()

checker = PlagiarismChecker()

file1 = "/home/shohruh/Shohruh/File/Library/Plagiat Checker/document1.txt"
file2 = "/home/shohruh/Shohruh/File/Library/Plagiat Checker/document1.docx"

file1_path = os.path.abspath(file1)
file2_path = os.path.abspath(file2)

print(f"File1 path: {file1_path}")
print(f"File2 path: {file2_path}")

if not os.path.exists(file1_path):
    raise FileNotFoundError(f"File not found: {file1_path}")
if not os.path.exists(file2_path):
    raise FileNotFoundError(f"File not found: {file2_path}")

try:
    text1 = read_file(file1_path)
    text2 = read_file(file2_path)
    similarity = checker.calculate_similarity(text1, text2)
    print(f"Similarity between files: {similarity:.2f}")
except Exception as e:
    print(f"An error occurred: {e}")
    utils.log_info(f"File o'qish muammo bor: {e}")
