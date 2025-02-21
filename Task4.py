class Book:
    def __init__(self,title,author,year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("~" * 40)

book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("Pride and Prejudice", "Jane Austen", 1949)
book3 = Book("Moby-Dick", "Herman Melville", 1851)

book1.describe()
book2.describe()
book3.describe()