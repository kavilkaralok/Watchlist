# loader.py
import json

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


# loader.py (continued)
def parse_data(data):
    parsed_data = []
    for movie in data:
        parsed_movie = {
            'title': movie['title'],
            'rank': int(movie['rank']),
            'id': movie['id']
        }
        parsed_data.append(parsed_movie)
    return parsed_data
