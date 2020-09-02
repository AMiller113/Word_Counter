import word_counter
import ui

if __name__ == "__main__":
    _ui = ui()
    _ui.handle_input()
    counter = WordCounter(_ui.file_name)
    success = counter.run()
    if success:
        _ui.display_word_count(counter)
        _ui.display_exit_message()
    else:
        _ui.display_error_message()
        exit()
