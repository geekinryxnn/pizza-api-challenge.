
from flask import jsonify, request
from server.app import app, db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'errors': ['Invalid restaurant_id or pizza_id']}), 400