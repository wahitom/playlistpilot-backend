from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to our postgresql db
engine = create_engine("postgresql://admin:GSSQIRooQyQnpUJkB0j0uPvQwPWfXbXK@dpg-clvgjnla73kc73bpiaog-a.frankfurt-postgres.render.com/playlists", echo=True)

# create connection with sessionmaker 
SessionLocal = sessionmaker(bind=engine) 

# define a method to get db 
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()