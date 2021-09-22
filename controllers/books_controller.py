import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)