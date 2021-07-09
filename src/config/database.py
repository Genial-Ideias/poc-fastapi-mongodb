from mongoengine import connect

from src.config.env import environment

DATABASE_URL = environment.get_item('DATABASE_URL')

def init_app():
    connect(host=DATABASE_URL)
