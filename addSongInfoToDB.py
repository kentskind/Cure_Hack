import sqlite3
from createSpotifyConnection import create_spotify_connection


def add_songinfo_to_db():

    db_filename = 'DreamTheater.db'
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    spotify = create_spotify_connection()

    albumIDs = c.execute('select SPOTIFY_ID, NAME from ALBUMDETAILS;')
    sql = 'insert into SONGDETAILS (SPOTIFY_ID, ALBUM_ID, NAME, DURATION_MS, TRACK_NUMBER) values (?,?,?,?,?)'

    for album in albumIDs.fetchall():
        print('Processing {}...'.format(album[1]))
        songs = spotify.album_tracks(album_id=album[0], limit=50)
        for song in songs['items']:
            songdata = (song['id'], album[0], song['name'], int(song['duration_ms']), int(song['track_number']))
            print(songdata)
            c.execute(sql, songdata)

    conn.commit()
    print("end")


if __name__ == '__main__':
    add_songinfo_to_db()
