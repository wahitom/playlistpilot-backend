#import it
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from models import Playlist
from schemas import PlaylistSchema


# initialize it
app = FastAPI()

# define a route 
@app.get('/')
def index():
    return {"message": "Welcome to my first api"}

# get all playlists
@app.get('/playlists')
def playlists(db: Session = Depends(get_db)):
    playlists = db.query(Playlist).all()
    return playlists

# get a single playlist 
@app.get('/playlists/{playlist_id}')
def playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = db.query(Playlist).filter(Playlist.id == playlist_id).first()
    return playlist

# create a playlist
@app.post('/playlists') 
def create_playlist(playlist: PlaylistSchema, db: Session = Depends(get_db)):
   # print(playlist)
    # the ** unpacks a dict and passes it as key value pairs 
    new_playlist = Playlist(**playlist.model_dump()) 
     # this will create a dict out of your info as it is being passed to the server

    
    # adds the playlist to the transaction ie one by one and if anything fails it all fails 
    db.add(new_playlist)
    # commit the transaction 
    db.commit()
    # get the playlist from the database again
    db.refresh(new_playlist)
    return {"message": "Playlist Created succesfully", "playlist": new_playlist}

#update a playlist
@app.patch('/playlists/{playlist_id}')
def updated_playlist(playlist_id: int):
    return {"message": f"Playlist {playlist_id} created successfully"}

# delete a playlist
@app.delete("/playlists/{playlist_id}")
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    deleted_playlist = db.query(Playlist).filter(Playlist.id == playlist_id).first()

    if deleted_playlist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Playlist {playlist_id} does not exist")
    else:
        deleted_playlist.delete()

        #run the transaction
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


