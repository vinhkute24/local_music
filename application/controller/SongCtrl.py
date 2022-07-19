from crypt import methods
from email.policy import default
from flask import Blueprint, jsonify, request, flash,redirect,url_for, send_file
import os
from werkzeug.utils import secure_filename
from flask.views import MethodView

import eyed3
from ..models.base import db

from ..models.song import Song
import glob



song = Blueprint('song', __name__, url_prefix="/song")


ALLOWED_EXTENSIONS = {'mp3', 'flac'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class SongUpload(MethodView):
    def get(self):
        pass
    
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = "/home/vinh/Desktop/test/back-end/"
            uploads_dir = os.path.join(path, 'music_src')
            file.save(os.path.join(uploads_dir, secure_filename(file.filename)))

            #extract mp3 tag 
            audio = eyed3.load(os.path.join(uploads_dir,secure_filename(file.filename)))
            song_title = audio.tag.title
            song_artist =audio.tag.artist
            file_src = os.path.join(uploads_dir, secure_filename(file.filename))
            

            #insert mp3 tag to database
            song = Song(song_title =song_title , song_artist=song_artist, file_src = file_src)
            db.session.add(song)
            db.session.commit()


            
        return jsonify({
            'message':'upload succesful'
        })
        
        
        

song.add_url_rule('/upload', methods=['POST'], view_func=SongUpload.as_view('upload'))


class GetMusic(MethodView):
    def get(self,id):
            tracks =[]
            existing_song = Song.query.get(id)
            

            for root, dirs, files, in os.walk("/home/vinh/Desktop/test/back-end/music_src"):  
                    for name in files:
                        if name.endswith((".mp3",".flac")):
                                path = "/home/vinh/Desktop/test/back-end/"
                                uploads_dir = os.path.join(path, 'music_src')
                                audio = eyed3.load(os.path.join(uploads_dir,name))
                                song_title = audio.tag.title
                                if song_title == existing_song.song_title:
                                    return send_file(os.path.join(uploads_dir,name))
                                #tracks.append(song_title)   


            """ for name_song in tracks:
                if name_song == existing_song.song_title:
                    song_dir = os.path.join(uploads_dir,name_song)
                    return send_file(os.path.join(uploads_dir,name_song)) """
         
            return jsonify({
                'error':'send file fail'
            })
    
    def post(self):
           pass

song.add_url_rule('/<int:id>', methods=['GET'], view_func=GetMusic.as_view('get_music'))



class GetList(MethodView):
    def get(self):
            list_songs = Song.query.filter(Song.file_src.endswith('.ogg')).all()
            result_array = []
            for song in list_songs:
                result_array.append(
                    dict(
                        id=song.id,
                        song_title=song.song_title,
                        song_artist = song.song_artist,
                        song_src = song.file_src
                    )
                )
            return jsonify({

                'songs': result_array,
                
            })
                    
    def post(self):
           pass

song.add_url_rule('/getList', methods=['GET'], view_func=GetList.as_view('get_list'))

