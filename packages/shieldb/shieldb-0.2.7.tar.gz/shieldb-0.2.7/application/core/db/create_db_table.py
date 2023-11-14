import os
from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import sessionmaker
from application import get_sqlalchemy_db_url

A = os.environ.get('SQLALCHEMY_DATABASE_URI')

database_url = get_sqlalchemy_db_url()
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = sqlalchemy.orm.declarative_base()


class TableCreation(Base):
    __tablename__ = 'test_table5'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    birth_date = Column(DateTime, default=datetime.utcnow)
    tc = Column(ARRAY(String), nullable=False)
    credit_card_number = Column(String, nullable=False)
    password = Column(JSONB, nullable=False)
    url = Column(String, nullable=False)
    number = Column(String, nullable=False)
    mix_content = Column(String, nullable=False)


Base.metadata.create_all(engine)


def add_to_table():
    for i in range(10):
        data = TableCreation(username="user123",
                             email="abcde@gmail.com ",
                             tc=['abcde@gmail.com', 'fghij@gmail.com'],
                             credit_card_number="4123456789012 4912345678901234 5624332432432432",
                             password={"history": [{"asds":"abc@gmail.com"}], "added_by": "abc@gmail.com Internal Service"},
                             url="https://chat.openai.com/",
                             number="0555915647 555-555-5555 +90 555 555 5555 ",
                             mix_content="12hfsjkhfd@gmail.com user1:12345 +90 555 555 5555 user2: 123456 "
                                    "21dsf@hotmail.io js slafd 54658998444 555-555-555")

        session.add(data)
    session.commit()


if __name__ == "__main__":
    add_to_table()
