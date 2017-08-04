"""Represent an employee in an organization."""

class Employee():
    """Represent an employee with no frills."""

    def __init__(self, first, last, salary):
        """Initialize attributes for the employee."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, sal_raise=5000):
        """Raise the employee's salary. If no raise given default to 5000."""

        self.salary += sal_raise
