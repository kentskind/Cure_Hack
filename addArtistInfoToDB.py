import sqlite3
from createSpotifyConnection import create_spotify_connection


def add_artistinfo_to_db():

    db_filename = 'Spotify_PreCure.db'
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    spotify = create_spotify_connection()

    artistIDs = c.execute('select artist_key from songs group by artist_key;')
    sql = 'insert into artists ' \
          '(artist_key, name, href_url, image_url_640) ' \
          'values (?,?,?,?)'

    for artist in artistIDs.fetchall():
        print(artist)
        print('Processing {}...'.format(artist[0]))
        artistDetail = spotify.artist(artist[0])
        print(artistDetail)
        image = artistDetail['images'][1]['url'] if len(artistDetail['images']) > 0 else None
        artistdata = (artist[0],
                      artistDetail['name'],
                      artistDetail['external_urls']['spotify'],
                      image)

        print(artistdata)
        c.execute(sql, artistdata)

    conn.commit()
    print('end')


if __name__ == '__main__':
    add_artistinfo_to_db()
