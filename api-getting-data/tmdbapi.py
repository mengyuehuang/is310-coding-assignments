import apikey

with open('C:\\Users\\98768\\Desktop\\is310\\api-getting-data\\apikeys.txt', 'r') as file:
    file.readline()
    second_line = file.readline().strip()

apikey.save("tmdb_key", second_line)
tmdb_api_key = apikey.load("tmdb_key")
#print(tmdb_api_key)


# select the 11th movie in the database - Star Wars
import requests
url = 'https://api.themoviedb.org/3/movie/11?api_key='
response = requests.get(url + tmdb_api_key)

tmdb_data = response.json()
import json
with open('api-getting-data/data/StarWars.json', 'w') as f:
    json.dump(tmdb_data, f)


# try finding Barbie
movie_name = 'Barbie'
url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={movie_name}"
response = requests.get(url)

tmdb_data = response.json()
with open('api-getting-data/data/Barbie.json', 'w') as f:
    json.dump(tmdb_data, f)