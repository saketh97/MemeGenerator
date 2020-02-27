class QuoteModel(object):

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        if self.body.startswith("\"").endswith("\""):
            return f'{self.body} - {self.author}'
        else:
            return f'"{self.body}" - {self.author}'
