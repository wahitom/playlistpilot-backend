#import it
from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Playlist, Song, User
from schemas import PlaylistSchema, UserSchema, SongSchema


# initialize it
app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
    )

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


# get all songs
@app.get('/songs')
def playlists(db: Session = Depends(get_db)):
    songs = db.query(Song).all()
    return songs



@app.post('/songs')
def song_added(song: SongSchema, db: Session = Depends(get_db)):
    # Check if a song exists on the playlist using its name
    existing_song = db.query(Song).filter(Song.name == song.name).first()

    if existing_song is None:
        # Song doesn't exist, so we create it
        new_song = Song(name=song.name, playlist_id=song.playlist_id)

        db.add(new_song)
        db.commit()
    
    else:
        # Check if the song already exists on the playlist
        duplicate_song = db.query(Song).filter(
            Song.playlist_id == song.playlist_id,
            Song.name == song.name
        ).first()

        if duplicate_song is None:
            # The song does not exist on the playlist, so we add it
            new_song = Song(name=song.name, playlist_id=song.playlist_id)

            db.add(new_song)
            db.commit()
        
        else:
            # If the playlist already has the song we are trying to add, throw an error
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Song already added to the playlist"
            )

    return {"message": "Song added successfully"}


