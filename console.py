from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book1 = Book("The Lord Of The Rings", "J.R.R. Tolkein")
book_repository.save(book1)

author1 = Author("J.R.R. Tolkein")
author_repository.save(author1)
