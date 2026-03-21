import csv

class Book:
    def __init__ (self, id, image_name,image_url,title,author,genre_id,genre):
        self.id = str(id)
        self.image_name = image_name
        self.image_url = image_url
        self.title = title
        self.author = author
        self.genre_id = int(genre_id)
        self.genre = genre

    def __str__(self):
        return f"{self.title:<50} - {self.author:<20} - {self.genre}"
    
def load_books(filename:str):
    """ Load books from a CSV file and return a list of Book objects."""
    books = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            books.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return books
    
if __name__ == "__main__":
    book = Book(1, "book1.jpg", "https://example.com/book1.jpg", "The Great Gatsby", "F. Scott Fitzgerald", 1, "Classic")
    print(book)
    books = load_books(r"C:\\Users\\emili\\OneDrive\\Desktop\\Curso_python ( no borrar )\\curso_python\\Books\\booklist2000.csv")
    print (books[3])
               