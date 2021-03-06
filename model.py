#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []


def init_bball(csv_file_name=BB_FILE_NAME):
    global bb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global bb_seasons
        bb_seasons = [] # reset, start clean
        for r in reader:
            bb_seasons.append(r)

def get_bball_seasons(sortby='year', sortorder='desc'):
    global bb_seasons
    return bb_seasons
