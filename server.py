import json

from flask import Flask, request

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.serializer import loads, dumps
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# Models
# ==========================

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    address = Column(String(300))


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('author.id'))
    message = Column(String(1000))


# SQLAlchemy boilerplate
# ==========================

engine = create_engine('postgresql+psycopg2://henry.jordan:fishy@localhost/cards')
Session = sessionmaker(bind=engine)
s = None

# Flask Boilerplate
# ==========================

application = Flask(__name__)

@application.before_request
def before_request():
    global s # Fix me later
    s = Session()


@application.teardown_request
def teardown_request(exception):
    if(exception):
        print(exception)

    global s # fix me later
    if s is not None:
        s.close()


# Flask Routes
# ==========================

@application.route('/api/')
def index():
    return "Welcome to my API"

@application.route('/api/author/', methods=['GET'])
def contact():
    author = s.query(Author).filter_by(name=request.args.get('name')).first()
    author_dict = dict()

    for k, v in author.__dict__.items():
        print(k)
        if k != "_sa_instance_state":
            author_dict[k] = v

    return str(json.dumps(author_dict))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=9999)
