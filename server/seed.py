from server.app import create_app
from models import db, User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    print("Seeding database...")

    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()

    user1 = User(username="host123", email="host@example.com")
    user1.password = "password123"

    user2 = User(username="admin456", email="admin@example.com")
    user2.password = "secure555"
    
    guest1 = Guest(name="Robert Downey Jr.")
    guest2 = Guest(name="Zendaya")
    guest3 = Guest(name="Taylor Swift")

    ep1 = Episode(title="Opening Night", date="2025-06-01")
    ep2 = Episode(title="Tech Talks", date="2025-06-10")

    appearance1 = Appearance(guest=guest1, episode=ep1, role="Main Guest")
    appearance2 = Appearance(guest=guest2, episode=ep2, role="Performer")
    appearance3 = Appearance(guest=guest3, episode=ep2, role="Surprise Guest")

    db.session.add_all([user1, user2, guest1, guest2, guest3, ep1, ep2, appearance1, appearance2, appearance3])
    db.session.commit()

    print("Done seeding!")
