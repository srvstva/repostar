import os


ENV = 'development'
DEBUG = True
SECRET_KEY = '54e7fdf6cd7c76cd1235bb3c98f6b083'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.dirname(os.path.abspath(__name__)) + '/development.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
