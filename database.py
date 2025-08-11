from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting / create an engine
sqlite_file_name = "blog.db"
sqlite_file_URL = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_file_URL, connect_args=connect_args)
print("DB URL:", engine.url)


# Mapping
Base = declarative_base()

#Session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
