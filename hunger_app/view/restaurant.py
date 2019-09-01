
from hunger_app.model.restaurant import Restaurant
from hunger_app import app, db, cors
from flask import jsonify, request
from hunger_app.schema.restaurant import RestaurantSchema
from flask import render_template
import datetime
import time
from itertools import cycle
import json
import decimal
import flask.json


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/restaurant/form', methods=['GET', 'POST'])
def restaurant_form():
    if request.method == 'GET':
        
        return render_template('donate.html')
    else:
        print(request.form.to_dict())
        post = Restaurant(**request.form.to_dict())
        post.save()
        result = RestaurantSchema().dump(post)
        return jsonify({'result': {'restaurant': result.data}, 'message': "Success", 'error': False})


@app.route('/restaurant/list', methods=['GET'])
def restaurant_list():
    if request.method == 'GET':
        args = request.form.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Restaurant.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantSchema(many=True).dump(data)
        print(result.data)
        return render_template("involve.html", data=result.data)


@app.route('/volunteer/form', methods=['GET', 'POST'])
def volunteer_form():
    if request.method == 'GET':
        return render_template('volunteer.html')
    else:
        result =request.form.to_dict()
        return jsonify({'result': {'restaurant': result.data}, 'message': "Success", 'error': False})