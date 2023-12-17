#import it
from fastapi import FastAPI
from schemas import PlaylistSchema


# initialize it
app = FastAPI()

# define a route 
@app.get('/')
def index():
    return {"message": "Welcome to my first api"}

# get all playlists
@app.get('/playlists')
def playlists():
    return []

# get a single playlist
@app.get('/playlists/{playlist_id}')
def playlist():
    return {}

# create a playlist
@app.post('/playlists') 
def create_playlist(playlist: PlaylistSchema):
    print(playlist)
    return {"message": "Playlist Created succesfully"}

#update a playlist
@app.patch('/playlists/{playlist_id}')
def updated_playlist(playlist_id: int):
    return {"message": f"Playlist {playlist_id} created successfully"}

# delete a playlist
@app.delete("/playlists/{playlist_id}")
def delete_playlist(playlist_id: int):
    return {"message" : f"Playlist {playlist_id} deleted successfully"} 


