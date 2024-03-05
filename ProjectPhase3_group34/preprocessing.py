import pandas as pd

def pre_artists():
    r_artists = 'C:\\Users\\anush\\Documents\\CSCI-620 Big ' \
                'Data\\Movies\\title.basics.tsv '
    artists = pd.read_table(r_artists)
    artists = artists.drop_duplicates()  # drop duplicates
    artists = artists.dropna()  # filter null values
    artists.to_csv('C:\\Users\\anush\\Documents\\CSCI-620 Big '
                   'Data\\Assignment 2\\director.csv', index=False,
                   header=False)
    print('Actor table preprocessed successfully')


def pre_albums():
    r_albums = 'C:\\Users\\anush\\Documents\\CSCI-620 Big ' \
               'Data\\Movies\\title.basics.tsv '
    albums = pd.read_table(r_albums)
    albums = albums.drop(['album_group'], axis=1)  # drop columns
    albums = albums.drop_duplicates()  # drop duplicates
    albums = albums.dropna()  # filter null values
    albums.to_csv('C:\\Users\\anush\\Documents\\CSCI-620 Big '
                  'Data\\Assignment 2\\director.csv', index=False,
                  header=False)
    print('Albums table preprocessed successfully')


def pre_tracks():
    r_tracks = 'C:\\Users\\anush\\Documents\\CSCI-620 Big ' \
               'Data\\Movies\\title.basics.tsv '
    tracks = pd.read_table(r_tracks)
    tracks = tracks.drop(['disc_number', 'preview_url'], axis=1)  # drop columns
    tracks = tracks.drop_duplicates()  # drop duplicates
    tracks = tracks.dropna()  # filter null values
    tracks.to_csv('C:\\Users\\anush\\Documents\\CSCI-620 Big '
                  'Data\\Assignment 2\\director.csv', index=False,
                  header=False)
    print('Tracks table preprocessed successfully')


def pre_audio_features():
    r_audio_features = 'C:\\Users\\anush\\Documents\\CSCI-620 Big ' \
                       'Data\\Movies\\title.basics.tsv '
    audio_features = pd.read_table(r_audio_features)
    # drop columns
    audio_features = audio_features.drop(['analysis_url', 'key', 'mode',
                                          'speechiness', 'tempo',
                                          'time_signature', 'valence'], axis=1)
    audio_features = audio_features.drop_duplicates()  # drop duplicates
    audio_features = audio_features.dropna()  # filter null values
    audio_features.to_csv('C:\\Users\\anush\\Documents\\CSCI-620 Big '
                          'Data\\Assignment 2\\director.csv', index=False,
                          header=False)
    print('Audio Features table preprocessed successfully')


def pre_genres():
    r_genres = 'C:\\Users\\anush\\Documents\\CSCI-620 Big ' \
               'Data\\Movies\\title.basics.tsv '
    genres = pd.read_table(r_genres)
    genres = genres.drop_duplicates()  # drop duplicates
    genres = genres.dropna()  # filter null values
    genres.to_csv('C:\\Users\\anush\\Documents\\CSCI-620 Big '
                  'Data\\Assignment 2\\director.csv', index=False,
                  header=False)
    print('Genres table preprocessed successfully')


def main():
    pre_artists()
    pre_albums()
    pre_tracks()
    pre_audio_features()
    pre_genres()