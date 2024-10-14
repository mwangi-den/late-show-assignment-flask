# models/appearance.py

# Importing the database instance
from db import db

class Appearance(db.Model):
    """Model representing a guest appearance on an episode."""

    __tablename__ = 'appearances'  # Define the table name in the database

    # Defining the columns in the appearances table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each appearance
    rating = db.Column(db.Integer, nullable=False)  # Rating given to the appearance (1-5)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)  # Foreign key linking to episodes
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)      # Foreign key linking to guests

    # Define relationships to allow easy access to associated episode and guest data
    episode = db.relationship('Episode', back_populates='appearances')  # Link to the Episode model
    guest = db.relationship('Guest', back_populates='appearances')      # Link to the Guest model

    def to_dict(self):
        """Convert the appearance instance to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id,
            'guest': self.guest.to_dict() if self.guest else None,  # Serialize related guest
            # Removed 'episode' to prevent recursion
        }

    @classmethod
    def validate_rating(cls, rating):
        """Validate that the rating is between 1 and 5."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")  # Raise error if the rating is invalid
