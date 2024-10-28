class publication:
    def __init__(self, name):
        self.name = name


class book(publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book Title: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class magazine(publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"Magazine Title: {self.name}")
        print(f"Editor: {self.editor}")


book = book("Compartment No. 6", "Rosa Liksom", 192)
magazine=magazine("Donald Duck", "Aki Hyyppä")
book.print_information()
magazine.print_information()
