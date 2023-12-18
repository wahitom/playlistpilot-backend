
#pydantic - allows us to create schemas of what our app accepts 
from pydantic import BaseModel


class PlaylistSchema(BaseModel):
    title: str
    description: str
    image : str
    rating : int 
    date_created : str

class UserSchema(BaseModel):
    name: str

class SongSchema(BaseModel):
    name : str
    playlist_id: int
 
