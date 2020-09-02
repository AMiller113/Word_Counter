class ui():
    def __init__(self):
        self.input_message = 'Please give the path to the txt file to get a word count.'
        self.exit_message = 'Thank you for using this program, farewell.'
        self.error_message = 'There has been an error, likely an invalid file path. Please restart the program.'
        self.file_name = ''

    def handle_input(self):
        self.file_name = input(self.input_message)

    def display_word_count(self, counter):
        sorted_dict = sorted(counter.word_count_dict.items(), key=lambda item: item[1], reverse=True)
        print('====================================================================================')
        for word, count in sorted_dict:
            print(f"{word}: {count}")

        print(f'\nTotal Tokens: {counter.total_token_count}')
        print(f'Total Words: {counter.total_word_count}')
        print(f'Total Words: {counter.unique_word_count}/n')

    def display_exit_message(self):
        print(self.exit_message)

    def display_error_message(self):
        print(self.error_message)
