from datetime import datetime
from flask import render_template, request, redirect, url_for, Blueprint
from services.service import RestService

rest_blueprint = Blueprint('rest', __name__)
rest_service = RestService()

@rest_blueprint.route('/')
def index():
    rest = rest_service.get_rest_name()
    return render_template('index.html',restaurants=rest )

@rest_blueprint.route('/', methods=['POST'])
def Post_rest():
    response = request.form
    rest_service.post_rest({
        'restaurant_id' : response.get("restaurant_id"),
        'name': response.get('name'),
        'email': response.get('email'),
        'phone': response.get('phone'),
        'num_guests': response.get('num_guests'),
        'date': response.get('date'),
        })
    reser = rest_service.get_reservation()
    return render_template('manage_reservations.html',reservations=reser)

@rest_blueprint.route('/cancel_reservation/<int:index>')
def Delete_rest(index):
    rest_service.delete(index)
    
    reser = rest_service.get_reservation()
    return render_template('manage_reservations.html',reservations=reser)