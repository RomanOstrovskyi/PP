from model import *

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
s = Session()

#tag1=Tag(id=1,name= "Text")
#tag2=Tag(id=2,name= "Text")

#add_user=User(id=1, username="Farr2", firstname="kate",  email="tddde@gmail.com", password="12344321", number="1")
#add_user2=User(id=2, username="Haha", firstname="Drake",  email="game@gmail.com", password="qwerwewew", number="2")

#notes1=Note(id=1,title="hi",text="text" , Tag_id=1, User_id=1)
#notes2=Note(id=2,title="git",text="text" , Tag_id=2, User_id=2)
#notes3=Note(id=3,title="git",text="text" , Tag_id=2, User_id=1)


#session.add(add_user)
#session.add(add_user2)
#session.add(tag1)
#session.add(tag2)
#session.add(notes3)
#session.add(editors3)
#session.add(editors1)
#session.add(editors2)
#session.add(notes1)
#session.add(notes2)
