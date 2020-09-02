import nltk
import re


class WordCounter():
    def __init__(self, file_name):
        self.file_name = '/content/drive/My Drive/Test Files/' + file_name
        self.tokens = []
        self.words = []
        self.word_count_dict = {}
        self.total_word_count = 0
        self.total_token_count = 0
        self.unique_word_count = 0
        nltk.download('punkt')

    def get_word_count_dict(self):
        pass

    def txt_tokenizer(self):
        try:
            file = open(self.file_name, mode='r')
        except:
            return False
        else:
            text = file.read()
            self.tokens = nltk.word_tokenize(text)
            return True

    def get_words(self):
        for token in self.tokens:
            print(token)
            if re.match('^[a-zA-Z0-9]+$', token):
                self.words.append(token)

    def count_tokens(self):
        self.total_token_count = len(self.tokens)

    def count_words(self):
        self.total_word_count = len(self.words)

    def count_unique_words(self):
        self.unique_word_count = len(set(self.words))
