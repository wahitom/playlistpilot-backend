from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, DateTime, Integer, TIMESTAMP

# create base model ie all other models are inheriting frm this one
Base = declarative_base()

# defining events model
class Playlist(Base):
    __tablename__ = "playlists"

    # define columns 
    id = Column(Integer(), primary_key = True)
    title = Column(Text(), nullable = False)
    description = Column(VARCHAR, nullable=False )
    image = Column(VARCHAR, nullable=False)
    rating = Column(Integer(), nullable = False)
    date_created = Column(VARCHAR, nullable = False)
    
