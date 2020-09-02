import word_counter
import ui

if __name__ == "__main__":
    _ui = ui()
    _ui.handle_input()
    counter = word_counter(_ui.file_name)
    success = counter.get_word_count()
    if success:
        _ui.display_word_count(counter.word_count_dict)
        _ui.display_exit_message()
    else:
        _ui.display_error_message()
        exit()
