import os


ENV = 'development'
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.dirname(os.path.abspath(__name__)) + '/development.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False