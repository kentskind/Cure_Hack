import sqlite3
from createSpotifyConnection import create_spotify_connection


def add_songinfo_to_db():

    db_filename = 'Spotify_PreCure.db'
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    spotify = create_spotify_connection()

    albumIDs = c.execute('select album_key, name from albums;')
    sql = 'insert into songs ' \
          '(song_key, artist_key, album_key, title, href_url, duration_ms, disk_number, track_number) ' \
          'values (?,?,?,?,?,?,?,?)'

    for album in albumIDs.fetchall():
        print('Processing {}...'.format(album[1]))
        songs = spotify.album_tracks(album_id=album[0], limit=50)
        for song in songs['items']:
            songdata = (song['id'],
                        song['artists'][0]['id'],
                        album[0], song['name'],
                        song['external_urls']['spotify'],
                        song['duration_ms'],
                        song['disc_number'],
                        song['track_number'])

            print(songdata)
            c.execute(sql, songdata)

    conn.commit()
    print("end")


if __name__ == '__main__':
    add_songinfo_to_db()
