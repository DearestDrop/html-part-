from flask import Flask, render_template, request, redirect, url_for, session, g
import config
from exts import db
from models import CdVinyls, User, Most_rating, Most_sailing, History
from blueprints.author import bp as auth_bp
from blueprints.cdvinyls import bp as cd_bp
from flask_migrate import Migrate
from search import imgurl, category_process
from forms import RegisterForm, LoginForm
import numpy as np
import random

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
with app.app_context():
    db.create_all()
app.register_blueprint(auth_bp)
app.register_blueprint(cd_bp)

migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def main():  # put application's code here
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(ratings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(ratings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if len(product.price) == 0 | len(product.price) > 10:
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_2.append(product)

    return render_template("Main.html", products_1=products_1, products_2=products_2)


@app.route('/loginpage', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if not user:
                print("not exist")
                return 'redirect1(url_for("login"))'
            if password == user.password:
                session['user_id'] = user.index
                return redirect(url_for("main"))
            else:
                return password
        else:
            print(form.errors)
            return 'redirect2(url_for("login"))'



@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


@app.route('/signuppage', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            print(form.errors)
            return form.errors


@app.route('/searchresult', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        product=[]
        return render_template('search.html',product=product)
    else:
        keywords = request.form['keywords']
        product = CdVinyls().query.filter(CdVinyls.title.like(keywords)).first()
        return render_template("search.html",product=product)



@app.route('/itemdetails1')
def detail1():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[0])


@app.route('/itemdetails2')
def detail2():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[1])


@app.route('/itemdetails3')
def detail3():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[2])

@app.route('/itemdetails4')
def detail4():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[3])

@app.route('/itemdetails5')
def detail5():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[4])


@app.route('/itemdetails6')
def detail6():
    index = 6
    ranurl = ['/static/1.png', '/static/2.png', '/static/3.png', '/static/4.png']
    products_1 = []
    products_2 = []
    sailings_id = []
    ratings_id = []
    for i in range(0,index):
        sail = Most_sailing.query.get(i + 1)
        rate = Most_rating.query.get(i + 1)
        sailings_id.append(sail.asin)
        ratings_id.append(rate.asin)
    i = 0
    for i in range(0,index):
        ran = random.choice([0, 1, 2, 3])
        if CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).count() == 0:
            i = i + 1
            index = index + 1
        product = CdVinyls.query.filter(CdVinyls.asin.like(sailings_id[i])).first()

        category = product.category
        imageURLHighRes = product.imageURLHighRes
        if imageURLHighRes == "[]":
            imageURLHighRes = ranurl[ran]
        if product.price == "":
            product.price = "$35.23"
        product.imageURLHighRes = imgurl(imageURLHighRes)
        product.category = category_process(category)
        products_1.append(product)

    return render_template("detail1.html", product=products_1[5])

@app.route('/myhistory', methods=['GET','POST'])
def history():
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    product = History.query.filter(History.username==user.username).all()
    return render_template("history.html", product=product)

if __name__ == '__main__':
    app.run()
