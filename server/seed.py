#!/usr/bin/env python3
from app import app, db, Movie

with app.app_context():
    print("Seeding database...")

    # Clear old data
    Movie.query.delete()

    # Add sample movies
    m1 = Movie(title="Inception", genre="Sci-Fi")
    m2 = Movie(title="The Dark Knight", genre="Action")
    m3 = Movie(title="Interstellar", genre="Sci-Fi")

    db.session.add_all([m1, m2, m3])
    db.session.commit()

    print("Seeding complete!")
