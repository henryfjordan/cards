from flask import Flask, request

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

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

engine = create_engine('postgresql+psycopg2://henry.jordan:fishy@localhost/endpoint')

a1 = Author(name="shia")
Session = sessionmaker(bind=engine)
s = Session()
s.add(a1)
s.commit()


application = Flask(__name__)

@application.route('/api/')
def index():
   return "Welcome to my API"

@application.route('/api/contact/', methods = ['POST'])
def contact():
   if request.method == 'POST':

      try:
         db_connection = psycopg2.connect(database='postgres', user='postgres')
         cursor = db_connection.cursor()
         cursor.execute("INSERT INTO messages (name, email, message) VALUES (%s, %s, %s);", (request.form.get('name'), request.form.get('email'), request.form.get('message')))
         db_connection.commit()
         cursor.close()
         db_connection.close()

      except psycopg2.DatabaseError, e:
         print "database error"
         return "Something broke in the DB"

       return "Thank you for your message, <b>" + request.form.get('name') + "</b>. I'll get back to you as soon as I can."

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8081)
