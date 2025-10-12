#!/usr/bin/python3
"""Module demonstrating polymorphism and method overriding in Python."""

import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Method to calculate area. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Return area of rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of circle."""
        return math.pi * (self.radius ** 2)
