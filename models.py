from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, DateTime, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, backref

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

    user_id = Column(Integer(), ForeignKey('users.id'))

    songs = relationship("Song", backref='playlist')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable = False) 


    playlists = relationship("Playlist", backref='user')


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)

    #foreign keys
    playlist_id = Column(Integer(), ForeignKey('playlists.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
