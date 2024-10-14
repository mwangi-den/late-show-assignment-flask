# models/guest.py

# Importing the database instance
from db import db

class Guest(db.Model):
    """Model representing a guest on the late show."""

    __tablename__ = 'guests'  # Define the table name in the database

    # Defining the columns in the guests table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each guest
    name = db.Column(db.String, nullable=False)     # Name of the guest
    occupation = db.Column(db.String, nullable=False)  # Guest's occupation

    # Define the relationship to appearances, allowing automatic deletion of related appearances
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

    def to_dict(self):
        """Convert the guest instance to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }
