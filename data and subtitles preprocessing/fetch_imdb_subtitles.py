import requests

credentials = {
  "username": "vasudhabm19",
  "password": "fWwL@2x4PruEgiM"
}

def getIMDBID(moviename):
    moviename = moviename.lower()
    url = f"https://www.omdbapi.com/?t={moviename}&apikey=68dd8045"
    response = requests.get(url)
    data = response.json()
    if 'Response' in data and data['Response'] == 'False':
        return (-1, -1)
    return (data["imdbID"], data["imdbRating"])


def subtitleAuthentication():
    url = "https://api.opensubtitles.com/api/v1/login"
    response = requests.post(url, json = credentials, headers = {"Api-Key": "9Q3t0YsFSJ4pK55yV4nQII74OGO4Xqq7"})
    response = response.json()
    token = response['token']
    return token


def getSubtitle(imdbID):
    url = f"https://api.opensubtitles.com/api/v1/subtitles?imdb_id={imdbID}"
    response = requests.get(url, headers = {"Api-Key": "9Q3t0YsFSJ4pK55yV4nQII74OGO4Xqq7"})
    data = response.json()
    data = data['data'][0]
    file_id = data['attributes']['files'][0]['file_id']
    return file_id

def downloadSubtitle(file_id):
    url = "https://api.opensubtitles.com/api/v1/download"
    response = requests.post(url, json = { "file_id" : file_id}, headers = {"Api-Key": "9Q3t0YsFSJ4pK55yV4nQII74OGO4Xqq7"})
    data = response.json()
    return data['link']




#Function calls to get imdb_id, rating and subtitles
imdbID, imdbRating = getIMDBID("Shawshank Redemption")

print(imdbID, imdbRating)

token = subtitleAuthentication()
file_id = getSubtitle(imdbID)
link = downloadSubtitle(file_id)

response = requests.get(link)
open(f"{imdbID}.srt", "wb").write(response.content)
