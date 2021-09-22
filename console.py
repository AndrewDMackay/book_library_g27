from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("J.R.R. Tolkein")
author_repository.save(author1)

book1 = Book("The Lord Of The Rings", author1)
book_repository.save(book1)

book2 = Book("The Hobbit", author1)
book_repository.save(book2)

