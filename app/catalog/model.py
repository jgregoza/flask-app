from app import db
from datetime import datetime

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        #return "<Title: {}>".format(self.title)
	    return 'Title: {}'.format(self.title)