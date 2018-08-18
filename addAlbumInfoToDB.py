import sqlite3
from typing import Dict, List, Any
from urllib.parse import urlparse, parse_qs
from createSpotifyConnection import create_spotify_connection


def add_albuminfo_to_db():

    db_filename = 'Spotify_PreCure.db'
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    sql = 'INSERT INTO albums ' \
          '(album_key, artist_key, name, href_url, image_url_300, release_date, release_date_precision, total_tracks) ' \
          'values (?,?,?,?,?,?,?,?)'

    spotify = create_spotify_connection()

    nextURL: object = 'initial'
    albumcount = 0

    while nextURL is not None:
        isInitial = True if nextURL == 'initial' else False
        next_qs = None if isInitial else parse_qs(urlparse(nextURL).query)
        offset = 0 if isInitial else next_qs['offset'][0]
        limit = 20 if isInitial else next_qs['limit'][0]

        results = spotify.search(q='プリキュア',
                                 type='album',
                                 offset=offset,
                                 limit=limit)

        for album in results['albums']['items']:
            # albumDetail = spotify.album(album["id"])
            print(album["name"])
            add_or_dont = input('Add {} to DB?[Y/n]'.format(album['name']))
            if add_or_dont in ['n', 'N', 'no', 'NO', 'No']:
                continue
            else:
                data = (album['id'],
                        album['artists'][0]['id'],
                        album['name'],
                        album['external_urls']['spotify'],
                        album['images'][1]['url'],
                        album['release_date'],
                        album['release_date_precision'],
                        album['total_tracks'])
                c.execute(sql, data)
                albumcount+=1

        if results['albums']['next']:
            nextURL = results['albums']['next']
        else:
            nextURL = None

    conn.commit()
    print('end')


if __name__ == '__main__':
    add_albuminfo_to_db()
