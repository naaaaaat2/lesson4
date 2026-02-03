class StringUtils:
    @staticmethod
    def is_palindrome(s):
        if not isinstance(s, str):
            return False
        return s == s[::-1]

    @staticmethod
    def count_words(s):
        if not isinstance(s, str):
            return 0
        return len(s.split())

    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            return None
        return s[::-1]
