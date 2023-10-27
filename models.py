from exts import db
from datetime import datetime

class CdVinyls(db.Model):
    __tablename__ = "product"
    index = db.Column(db.Integer, primary_key=True,autoincrement=True)
    category = db.Column(db.Text)
    tech1 = db.Column(db.Text)
    description = db.Column(db.Text)
    fit = db.Column(db.Text)
    title = db.Column(db.Text)
    also_buy = db.Column(db.Text)
    tech2 = db.Column(db.Text)
    brand = db.Column(db.Text)
    feature = db.Column(db.Text)
    rank = db.Column(db.Text)
    also_view = db.Column(db.Text)
    main_cat = db.Column(db.Text)
    similar_item = db.Column(db.Text)
    date = db.Column(db.Text)
    price = db.Column(db.Text)
    asin = db.Column(db.Text)
    imageURL = db.Column(db.Text)
    imageURLHighRes = db.Column(db.Text)
class User(db.Model):
    __tablename__ = "user"
    index = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class History(db.Model):
    __tablename__ = "history"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    asin = db.Column(db.Text)
    imageURL = db.Column(db.Text)
    title = db.Column(db.Text)
    category = db.Column(db.Text)
    brand = db.Column(db.Text)

class Most_rating(db.Model):
    __tablename__ = "most_rating"
    index = db.Column(db.Integer, primary_key=True,autoincrement=True)
    asin = db.Column(db.Text)
    ave_rating = db.Column(db.Float)


class Most_sailing(db.Model):
    __tablename__ = "most_sailing"
    index = db.Column(db.Integer, primary_key=True,autoincrement=True)
    asin = db.Column(db.Text)
    _counts = db.Column(db.Float)
    reviewerID_counts = db.Column(db.Float)
    total = db.Column(db.Float)
