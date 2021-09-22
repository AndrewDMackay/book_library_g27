from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['user_id'])
        author = Author(row['name'], user )
        author.append(authors)
    return authors


# def select(id):
#     task = None
#     sql = "SELECT * FROM tasks WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         user = user_repository.select(result['user_id'])
#         task = Task(result['description'], user, result['duration'], result['completed'], result['id'] )
#     return task


# def update(task):
#     sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user.id, task.duration, task.completed, task.id]
#     run_sql(sql, values)
