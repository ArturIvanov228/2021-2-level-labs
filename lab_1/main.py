"""
Lab 1
Language detection
"""


def tokenize(text: str) -> list or None:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation and other symbols from words
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """

    if isinstance(text, str):  # text является экземпляром классом str
        text = text.lower()  # перевод строки в нижний регистр
        for char in text:
            if char != ' ' and not (char.isalpha()):  # проверка то,что символ не пробел и не является буквой
                text = text.replace(char, "")  # удаление этого символа

        tokens = text.split()
        if not tokens:
            return None
        else:
            return tokens


def remove_stop_words(tokens: list, stop_words: list):
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :param stop_words.words(language): a list of stop words
    :return: a list of tokens without stop words
    """
    if isinstance(tokens, list) and isinstance(stop_words, list):
        if tokens:
            for j in range(len(tokens)):
                if tokens[j] in stop_words:
                    tokens[j] = ''

            while '' in tokens:
                tokens.remove('')
            return tokens
        else:
            return None
    else:
        return None

    


def calculate_frequencies(tokens: list) -> dict or None:
    """
      Calculates frequencies of given tokens
      :param tokens: a list of tokens
      :return: a dictionary with frequencies
      """
    if isinstance(tokens, list):
        dict_frequencies = {}
        for token in tokens:
            if isinstance(token, str):
                if token in dict_frequencies:
                    dict_frequencies[token] += 1
                else:
                    dict_frequencies[token] = 1
        if dict_frequencies:
            return dict_frequencies
        else:
            return None
    else:
        return None


def get_top_n_words(freq_dict: dict, top_n: int) -> list or None:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words
    :return: a list of the most common words
    """
    pass


def create_language_profile(language: str, text: str, stop_words: list) -> dict or None:
    """
    Creates a language profile
    :param language: a language
    :param text: a text
    :param stop_words: a list of stop words
    :return: a dictionary with three keys – name, freq, n_words
    """
    pass


def compare_profiles(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> float or None:
    """
    Compares profiles and calculates the distance using top n words
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: the distance
    """
    pass


def detect_language(unknown_profile: dict, profile_1: dict, profile_2: dict, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary
    :param profile_1: a dictionary
    :param profile_2: a dictionary
    :param top_n: a number of the most common words
    :return: a language
    """
    pass


def compare_profiles_advanced(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> list or None:
    """
    Compares profiles and calculates some advanced parameters
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: a dictionary with 7 keys – name, score, common, sorted_common, max_length_word,
    min_length_word, average_token_length
    """
    pass


def detect_language_advanced(unknown_profile: dict, profiles: list, languages: list, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile within the list of possible languages
    :param unknown_profile: a dictionary
    :param profiles: a list of dictionaries
    :param languages: a list of possible languages
    :param top_n: a number of the most common words
    :return: a language
    """
    pass


def load_profile(path_to_file: str) -> dict or None:
    """
    Loads a language profile
    :param path_to_file: a path
    :return: a dictionary with three keys – name, freq, n_words
    """
    pass


def save_profile(profile: dict) -> int:
    """
    Saves a language profile
    :param profile: a dictionary
    :return: 0 if everything is ok, 1 if not
    """
    pass
