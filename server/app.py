# server/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models and controllers
# from models import restaurant, pizza, restaurant_pizza
# from controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

if __name__ == '__main__':
    app.run(debug=True)