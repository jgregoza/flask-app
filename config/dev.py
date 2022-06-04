DEBUG = True
SECRET_KEY = 'postgres',
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/book_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# app.config.from_object('configuration.DevelopmentConfig')
# db =SQLAlchemy(app)

