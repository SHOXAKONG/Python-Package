import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .file_reader import read_file

class PlagiarismChecker:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', text.strip().lower())

    def calculate_similarity(self, text1, text2):
        """Calculates similarity between two pieces of text."""
        texts = [self.clean_text(text1), self.clean_text(text2)]
        tfidf_matrix = self.vectorizer.fit_transform(texts)
        return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    def check_file(self, file_path, reference_text):
        file_text = read_file(file_path)
        return self.calculate_similarity(file_text, reference_text)
