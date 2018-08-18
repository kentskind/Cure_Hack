import os
import sqlite3


def db_initial_settings():

    db_filename = 'DreamTheater.db'

    db_is_new = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)

    if db_is_new:
        print('Need to create Schema')
    else:
        print('Database exists.')

    create_tables(conn)


def create_tables(conn):
    conn.execute('create table PLAYLISTS('
                 'id integer primary key autoincrement, '
                 'playlist_id text, '
                 'isanalysed integer, '
                 'fetchdate text, '
                 'analysedate text, '
                 'number_of_songs integer)')

    conn.execute('create table SONGS('
                 'id integer primary key autoincrement, '
                 'song_id integer, '
                 'songindex integer')

    conn.execute('create table ALBUMDETAILS('
                 'id integer primary key autoincrement, '
                 'name text, '
                 'release_date text')

    conn.execute('create table SONGDETAILS('
                 'id integer primary key autoincrement, '
                 'name text, '
                 'album_id integer, '
                 'length integer')




if __name__ == '__main__':
    db_initial_settings()
