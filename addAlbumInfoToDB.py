import sqlite3
from createSpotifyConnection import create_spotify_connection


def add_albuminfo_to_db():

    db_filename = 'DreamTheater.db'
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    sql = 'INSERT INTO albums ' \
          '(album_key, artist_key, name, href_url, image_url_300, release_date, release_date_precision, total_tracks) ' \
          'values (?,?,?,?,?,?,?,?)'

    spotify = create_spotify_connection()

    albumdata = spotify.artist_albums(artist_id='2aaLAng2L2aWD2FClzwiep', limit=50, album_type='album')

    print(len(albumdata['items']))

    sql = 'insert into ALBUMDETAILS (SPOTIFY_ID, NAME, RELEASE_DATE) values (?,?,?);'

    for album in albumdata['items']:
        data = (album['id'], album['name'], album['release_date'])
        c.execute(sql, data)

    conn.commit()


if __name__ == '__main__':
    add_albuminfo_to_db()
