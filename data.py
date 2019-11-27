import pandas as pd


def get_stations_txt_as_df(filepath):
    """For processing ghcnd-stations.txt"""
    colspecs = [
        (1,11), (13,20), (22,30), (32,37), (39,40), (42,71), (73,75), (77,79), (81,85)
    ]
    names = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name', 'gsn flag', 'hcn crn flag', 'wmo id',]

    return pd.read_fwf(names=names, filepath_or_buffer=filepath, colspecs=colspecs)
