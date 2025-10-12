#!/usr/bin/python3
"""Module defining a Book class using Python magic methods."""

class Book:
    """A class to represent a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
