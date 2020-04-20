class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return("{} by {}".format(self.title, self.author))


class PaperBook(Book):
    def __init__(self, title, author, numpages):
        Book.__init__(self, title, author)
        self.pagecount = numpages


class Ebook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size


class Library:
    def __init__(self):
        self.books = []

    def addBooks(self, book):
        self.books.append(book)

    def NumOfBooks(self):
        return(len(self.books))


if __name__ == "__main__":
    MyBook = Ebook("Getting things done", "David Allen", 2)
    MypaperBook = PaperBook("Getting things done", "David Allen", 590)
    # print(MyBook.size)
    # print(MypaperBook.pagecount)
    Library = Library()
    Library.addBooks(MyBook)
    Library.addBooks(MypaperBook)
    print(Library.NumOfBooks())
