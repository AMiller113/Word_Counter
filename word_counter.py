import nltk
import re

# TODO find a way to remove tokens that are not actually words


class WordCounter():
    def __init__(self, file_name):
        self.file_name = file_name
        self.tokens = []
        self.words = []
        self.word_count_dict = {}
        self.total_word_count = 0
        self.total_token_count = 0
        self.unique_word_count = 0
        nltk.download('punkt') # TODO find a way to deactivate after first use

    def run(self):
        success = self.txt_tokenizer()
        if not success:
            return False
        self.get_words()
        self.get_word_count_dict()
        self.count_tokens()
        self.count_words()
        self.count_unique_words()
        return success

    def get_word_count_dict(self):
        for word in self.words:
            if word not in self.word_count_dict:
                self.word_count_dict[word] = 1
            else:
                self.word_count_dict[word] += 1

    def txt_tokenizer(self):
        try:
            file = open(self.file_name, mode='r', encoding='utf-8')
        except:
            return False
        else:
            text = file.read()
            self.tokens = nltk.word_tokenize(text)
            return True

    def get_words(self):
        for token in self.tokens:
            if re.match('^[a-zA-Z0-9]+$', token):
                self.words.append(token)

    def count_tokens(self):
        self.total_token_count = len(self.tokens)

    def count_words(self):
        self.total_word_count = len(self.words)

    def count_unique_words(self):
        self.unique_word_count = len(set(self.words))
