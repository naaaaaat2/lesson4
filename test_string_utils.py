from string_utils import StringUtils


def test_is_palindrome_positive():
    assert StringUtils.is_palindrome("radar")
    assert StringUtils.is_palindrome("level")
    assert StringUtils.is_palindrome("А роза упала на лапу Азора")


def test_is_palindrome_negative():
    assert not StringUtils.is_palindrome("hello")
    assert not StringUtils.is_palindrome("")
    assert not StringUtils.is_palindrome(None)
    assert not StringUtils.is_palindrome(12345)


def test_count_words_positive():
    assert StringUtils.count_words("Это тестовая строка") == 4
    assert StringUtils.count_words("один два три") == 3
    assert StringUtils.count_words("  много   пробелов  ") == 3


def test_count_words_negative():
    assert StringUtils.count_words("") == 0
    assert StringUtils.count_words(" ") == 0
    assert StringUtils.count_words(None) == 0
    assert StringUtils.count_words(12345) == 0


def test_reverse_string_positive():
    assert StringUtils.reverse_string("abc") == "cba"
    assert StringUtils.reverse_string("12345") == "54321"
    assert StringUtils.reverse_string("Тест") == "тесТ"


def test_reverse_string_negative():
    assert StringUtils.reverse_string(None) is None
    assert StringUtils.reverse_string(12345) is None


def test_reverse_string_empty():
    assert StringUtils.reverse_string("") == ""


def test_is_palindrome_with_spaces():
    long_str = "А роза упала на лапу Азора".replace(" ", "").lower()
    assert StringUtils.is_palindrome(long_str)
