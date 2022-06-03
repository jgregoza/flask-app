DEBUG = True
SECRET_KEY = 'topsecret',
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:topsecret@localhost:5432/mydatabase'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# app.config.from_object('configuration.DevelopmentConfig')
# db =SQLAlchemy(app)

