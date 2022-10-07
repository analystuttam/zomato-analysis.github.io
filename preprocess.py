import pandas as pd

def show(df):
    new = df.copy()
    try:
        new.drop(['Unnamed: 0', 'establishment', 'url', 'address', 'city', 'state.1', 'locality', 'latitude', 'longitude',
              'timings', 'highlights', 'photo_count', 'takeaway'], axis=1, inplace=True)
    except:
        pass
    return new