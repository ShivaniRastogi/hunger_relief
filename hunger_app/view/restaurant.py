
from hunger_app.model.restaurant import Restaurant
from hunger_app import app, db, cors
from flask import jsonify, request
from hunger_app.schema.restaurant import RestaurantSchema
from flask import render_template, redirect
import datetime
import time
from itertools import cycle
import json
import decimal
import flask.json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/restaurant/form', methods=['GET', 'POST'])
def restaurant_form():
    if request.method == 'GET':
        return render_template('donate.html')
    else:
        post = Restaurant(**request.form.to_dict())
        post.save()
        return redirect(str(app.config["APP_URL"]) + '/restaurant/list', code=302)


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
        return render_template("involve.html", data=result.data)


@app.route('/restaurant/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_id(id):
    if request.method == 'PUT':
        put = Restaurant.query.filter_by(id=id).update(request.json)
        if put:
            Restaurant.update_db()
            s = Restaurant.query.filter_by(id=id).first()
            result = RestaurantSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        res = Restaurant.query.filter_by(id=id).first()
        if not res:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Restaurant.delete_db(res)
        return jsonify({'result': {}, 'message': "Success", 'error': False})





@app.route('/volunteer/form', methods=['GET', 'POST'])
def volunteer_form():
    if request.method == 'GET':
        return render_template('volunteer.html')
    else:
        result = request.form.to_dict()
        gmail_user = "sharmaabhi069.as@gmail.com"
        gmail_pwd = "9891808371"
        # html = """\
        #       <html>
        #           <head></head>
        #           <body>
        #           <h1>hellloooo</h1>
        #           </body>
        #       </html>
        #       """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        msg = MIMEMultipart()
        msg['Subject'] = "Volunteer assigned for pickup"
        msg['From'] = gmail_user
        text = '''Dear , ''' + str(result["name"]) + '''hunger relief is thankful for your support.
        Millions of our fellow beings are dying in hunger while millions of tons of food is being wasted, thrown away and discarded.
        with support of each other we can ensure no one goes to sleep empty stomach
        this is the great way to serve humanity
        We are thankfull for your donation'''
        + str(result["contact_no"]) + '''contact no of our volunteer'''
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        # part2 = MIMEText(html, 'html')
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        # msg.attach(part2)
        msg['To'] = str(result["res_email"])
        response = server.sendmail(gmail_user, str(result["res_email"]), msg.as_string())
        server.quit()
        return jsonify({'result': {'response': response}, 'message': "Success", 'error': False})