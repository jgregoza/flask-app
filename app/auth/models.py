from app import db, bcrypt  # app/__init__.py
from flask_login import UserMixin
from app import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Colum(db.Integer, primary_key=True)
    user_name = db.Colum(db.String(20))
    user_email = db.Colum(db.String(60), unique=True, index=True)
    user_password = db.Colum(db.String(70))

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)
        

    @classmethod
    def create_user(cls, user, email, password):

        user = cls(user_name=user, 
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8') 
                  )

        db.session.add(user)
        db.session.commit()
        return user

@login_manager.user_loader  # stores the active user's ID
def load_user(id):
    return User.query.get(int(id))