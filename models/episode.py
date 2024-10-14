# models/episode.py

# Importing the database instance
from db import db

class Episode(db.Model):
    """Model representing an episode of the late show."""

    __tablename__ = 'episodes'  # Define the table name in the database

    # Defining the columns in the episodes table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each episode
    date = db.Column(db.String, nullable=False)     # Date when the episode aired
    number = db.Column(db.Integer, nullable=False)   # Episode number

    # Define the relationship to appearances, allowing automatic deletion of related appearances
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def to_dict(self):
        """Convert the episode instance to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [appearance.to_dict() for appearance in self.appearances]  # Serialize appearances
        }
