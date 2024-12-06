class Book:  
    def __init__(self, title, author, pages):  
        self.title = title  
        self.author = author  
        self.pages = pages  
        self.is_read = False  

    def read(self):  
        self.is_read = True  
        print(f"You have read '{self.title}' by {self.author}.")  

    def summary(self):  
        status = "Read" if self.is_read else "Not Read"  
        return f"'{self.title}' by {self.author}, {self.pages} pages - Status: {status}"  


class EBook(Book):  
    def __init__(self, title, author, pages, file_size):  
        super().__init__(title, author, pages)  
        self.file_size = file_size  # in Megabytes  

    def summary(self):  
        base_summary = super().summary()  
        return f"{base_summary}, File Size: {self.file_size} MB"  


# Example usage  
def book_demo():  
    my_book = Book("1984", "George Orwell", 328)  
    print(my_book.summary())  
    my_book.read()  
    print(my_book.summary())  

    my_ebook = EBook("The Invisible Man", "H.G. Wells", 200, 1.5)  
    print(my_ebook.summary())  
    my_ebook.read()  
    print(my_ebook.summary())  

book_demo()