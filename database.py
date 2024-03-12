from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from datetime import datetime

class Base(DeclarativeBase):
    pass


class Punch(Base):
    __tablename__ = "punch"

    id = Column(Integer, primary_key=True)
    student_name = Column(String(64))
    timestamp = Column(DateTime, default=datetime.utcnow())


# Replace 'sqlite:///my_database.db' with your actual database connection string
engine = create_engine('sqlite:///my_class.db')

Session = sessionmaker(bind=engine)

def add_punch(name):
    with Session() as s:
        p = Punch()
        p.student_name = name
        s.add(p)
        s.commit()


# Create the table
# Base.metadata.create_all(engine)

