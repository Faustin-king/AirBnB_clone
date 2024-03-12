# Import necessary modules
import math
import os


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def display_info(self):
        """Display information about the circle."""
        print(f"Circle with radius {self.radius}")
        print(f"Area: {self.calculate_area()}")


def main():
    # Get user input for the circle's radius
    radius = float(input("Enter the radius of the circle: "))

    # Create a Circle object
    circle = Circle(radius)

    # Display information about the circle
    circle.display_info()


if __name__ == "__main__":
    main()

