# server/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False