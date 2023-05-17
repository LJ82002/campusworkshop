"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7j05269vf5qb7l8s0-a.oregon-postgres.render.com",
        database="todo_m393",
        user="root",
        password="GYJiF3bgMTT6QnFZOS52vNWDBMe549Sx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
