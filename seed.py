from models import PlaylistSong, db, Playlist, Song
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Playlist.query.delete()
Song.query.delete()

playlist1 = Playlist(name = 'mc', description = 'this is a Mariah Carey playlist')

playlist2 = Playlist(name = 'Dance Party', description = 'this is a Dance Party playlist')


db.session.add(playlist1)
db.session.add(playlist2)


song1 = Song(title = 'Dreamlover', artist = 'Mariah Carey')
song2 = Song(title = 'Emotions', artist = 'Mariah Carey')
song3 = Song(title = 'Always be my baby', artist = 'Mariah Carey')
song4 = Song(title = 'heartbreaker', artist = 'Mariah Carey')
song5 = Song(title = 'Lonley', artist = 'Joel Corey')
song6 = Song(title = 'When Youre gone', artist = 'Shawn Mendez')
song7 = Song(title = 'POV', artist = 'Ariana Grande')

db.session.commit()

db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.add(song4)
db.session.add(song5)
db.session.add(song6)
db.session.add(song7)

db.session.commit()

playlist_add1 = PlaylistSong(playlist_id = playlist1.id, song_id = song1.id)
playlist_add2 = PlaylistSong(playlist_id = playlist1.id, song_id = song2.id)
playlist_add3 = PlaylistSong(playlist_id = playlist1.id, song_id = song3.id)
playlist_add4 = PlaylistSong(playlist_id = playlist1.id, song_id = song4.id)

playlist_add5 = PlaylistSong(playlist_id = playlist2.id, song_id = song5.id)
playlist_add6 = PlaylistSong(playlist_id = playlist2.id, song_id = song6.id)
playlist_add7 = PlaylistSong(playlist_id = playlist2.id, song_id = song7.id)

db.session.add(playlist_add1)
db.session.add(playlist_add2)
db.session.add(playlist_add3)
db.session.add(playlist_add4)
db.session.add(playlist_add5)
db.session.add(playlist_add6)
db.session.add(playlist_add7)

db.session.commit()