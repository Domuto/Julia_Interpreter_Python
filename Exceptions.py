class LexicalAnalyzerException(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error


class ParseException(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error

