#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import sessionmaker

from model import *


session = sessionmaker(bind=engine)

category1=Category(id=3, name="text")
category2=Category(id=4, name="text")

tag1=Tag(id=7,name= "Text")
tag2=Tag(id=8,name= "Text")

add_user=User(id=5, username="Farr2", firstname="kate",  email="tddde@gmail.com", password="12344321", number="1")
add_user2=User(id=6, username="Haha", firstname="Drake",  email="game@gmail.com", password="qwerwewew", number="2")





notes1=Notes(id=5,title="hi",text="text" , Tag_id=1, User_id=1, Category_id=1)
notes2=Notes(id=6,title="git",text="text" , Tag_id=2, User_id=2, Category_id=2)

editors1=Editors(id=5,Notes_id= 1,User_id= 1)
editors2=Editors(id=6,Notes_id= 2,User_id= 2)
ss = session()

ss.add(add_user)
ss.add(add_user2)
ss.add(tag1)
ss.add(tag2)

ss.add(category1)
ss.add(category2)
ss.add(editors1)
ss.add(editors2)
ss.add(notes1)
ss.add(notes2)



ss.commit()