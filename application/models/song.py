from email.policy import default
from .base import db


class Song(db.Model):
    __tablename__='song'
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(150), nullable=False)
    song_artist = db.Column(db.String(150), nullable=False)
    file_src = db.Column(db.String(150), nullable=False)
    # album = db.Column(db.String(150), unique=True, nullable=False)
    
   

    def __init__(self, song_title, song_artist, file_src ):
        self.song_title = song_title
        self.song_artist = song_artist
        self.file_src = file_src

