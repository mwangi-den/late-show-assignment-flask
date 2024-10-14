from flask import Flask 
from models.episode import Episode 
from models.guest import Guest
from models.appearance import Appearance
from db import db 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def populate_tables():
    """Populate the database with initial data for Guests and Episodes.

    This function creates the database tables, drops existing tables if any,
    and adds a predefined set of guest and episode data to the database.
    """
    with app.app_context():  
        db.drop_all()  
        db.create_all()  
        guest_data = [
            ('Michael J. Fox', 'actor'),
            ('Sandra Bernhard', 'Comedian'),
            ('Tracey Ullman', 'television actress'),
            ('Gillian Anderson', 'film actress'),
            ('David Alan Grier', 'actor'),
            ('William Baldwin', 'actor'),
            ('Michael Stipe', 'Singer-lyricist'),
            ('Carmen Electra', 'model'),
            ('Matthew Lillard', 'actor'),
            ('David Cross', 'stand-up comedian'),
            ('Yasmine Bleeth', 'actress'),
            ('D. L. Hughley', 'actor'),
            ('Rebecca Gayheart', 'television actress'),
            ('Steven Wright', 'Comedian'),
            ('Amy Brenneman', 'actress'),
            ('Melissa Gilbert', 'actress'),
            ('Cathy Moriarty', 'actress'),
            ('Louie Anderson', 'comedian'),
            ('Sarah Michelle Gellar', 'actress'),
            ('Melanie C', 'Singer-songwriter'),
            ('Greg Proops', 'actor'),
            ('Maury Povich', 'television personality'),
            ('Brooke Shields', 'actress'),
            ('Molly Shannon', 'Comic'),
            ('Chris O\'Donnell', 'actor'),
            ('Christina Ricci', 'actress'),
            ('Tori Amos', 'Singer-songwriter'),
            ('Yasmine Bleeth', 'actress'),
            ('Bill Maher', 'comedian'),
            ('Jennifer Love Hewitt', 'actress'),
            ('Goo Goo Dolls', 'rock band'),
            ('Dave Grohl', 'musician'),
            ('Stephen Rea', 'Film actor'),
            ('Roshumba Williams', 'Model'),
            ('Kellie Martin', 'television actress'),
            ('Kathy Griffin', 'actress'),
            ('Laura San Giacomo', 'actress'),
            ('Joan Lunden', 'journalist'),
            ('Shannen Doherty', 'actress'),
            ('Greatest Millennium Special', 'NA'),
            ('George Carlin', 'comedian'),
            ('Michael Boatman', 'actor'),
            ('David Boreanaz', 'actor'),
            ('Jewel', 'singer-songwriter'),
            ('Paul Rudd', 'actor'),
            ('Senator Bob Dole', 'us senator'),
            ('Senator Bob Dole', 'us senator'),
            ('Rob Schneider', 'actor'),
            ('George Carlin', 'comedian'),
            ('Pamela Anderson, Natalie Raitano, Molly Culver', 'actress'),
            ('Daniel Stern', 'film actor'),
            ('Melina Kanakaredes', 'actress'),
            ('Ed McMahon', 'comedian'),
            ('Mike Judge', 'actor'),
            ('Dave Foley', 'actor'),
            ('Kellie Martin', 'television actress'),
            ('Jerry O\'Connell', 'actor'),
            ('Melissa Gilbert', 'actress'),
            ('Brendan Fraser', 'actor'),
            ('John Tesh', 'pianist'),
            ('Sammy Hagar', 'Vocalist'),
            ('Hootie & the Blowfish, Billy Crystal', 'rock band'),
            ('Hootie & the Blowfish, Billy Crystal', 'actor'),
            ('Peter Krause', 'Film actor'),
            ('Chris Isaak', 'musician'),
            ('Frank DeCaro\'s Oscar Special, John Larroquette', 'writer'),
            ('Frank DeCaro\'s Oscar Special, John Larroquette', 'actor'),
            ('Joseph Gordon-Levitt', 'actor'),
            ('Eric McCormack', 'actor'),
            ('Jennifer Grey', 'actress'),
            ('Norm Macdonald', 'Stand-up comedian'),
            ('Dweezil Zappa', 'musician'),
            ('Maya Rudolph', 'actor'),
            ('Jon Cryer', 'actor'),
            ('Joan Baez', 'singer-songwriter'),
            ('Dan Aykroyd', 'actor'),
            ('Brian Dennehy', 'actor'),
            ('Woody Allen', 'film actor'),
            ('Charlie Sheen', 'actor'),
            ('John Malkovich', 'film actor'),
        ]

        for name, occupation in guest_data:
            guest = Guest(name=name, occupation=occupation)
            db.session.add(guest)  
        episode_data = [
            ('1/5/99', 1),
            ('1/12/99', 2),
            ('1/19/99', 3),
            ('1/26/99', 4),
            ('2/2/99', 5),
            ('2/9/99', 6),
            ('2/16/99', 7),
            ('2/23/99', 8),
            ('3/2/99', 9),
            ('3/9/99', 10),
        ]
        for date, number in episode_data:
            episode = Episode(date=date, number=number)
            db.session.add(episode)  
        appearance_data = [
            (1, 1, 5),  
            (2, 2, 6),
            (3, 3, 7),
            (4, 4, 8),
            (5, 5, 9),
        ]
        for rating, episode_id, guest_id in appearance_data:
            Appearance.validate_rating(rating)

            appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
            db.session.add(appearance)  
        db.session.commit() 

if __name__ == '__main__':
    populate_tables()  