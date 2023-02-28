from  flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class AutolabelModel(db.Model):
    __tablename__ = "autolabels"

    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), unique=True)
    country = db.Column(db.String(100), nullable = False)
    foundation_year=db.Column(db.Integer)
    liqudation_year = db.Column(db.Integer)
    avatar_path=db.Column(db.String(100))
    models = db.relationship('AutomodelsModel', backref="producer")

    def __init__(self,label,country,f_year,l_year=None):
        self.label=label
        self.country= country
        self.foundation_year=f_year
        self.liqudation_year=l_year
        self.avatar_path=f"img/labels/{self.label}.png"

    def __repr__(self):
        return f"{self.label} was founded in {self.country} in {self.foundation_year}"


class AutomodelsModel(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), unique=True)
    prod_id = db.Column(db.Integer(),db.ForeignKey('autolabels.id'))
    start_prod_year=db.Column(db.Integer)
    end_prod_year = db.Column(db.Integer)
    lots = db.relationship('LotModel', backref="model")

    def __init__(self,label, prod_id, f_year, l_year=None):
        self.label=label
        self.prod_id=prod_id
        self.start_prod_year=f_year
        self.end_prod_year=l_year

    def __repr__(self):
        return f"{self.label} was model for {self.producer.label} and production started in {self.start_prod_year}"

class LotModel(db.Model):
    __tablename__="lots"

    id=db.Column(db.Integer, primary_key=True)
    model_id=db.Column(db.Integer(),db.ForeignKey('models.id'))
    price=db.Column(db.Integer, nullable=False)
    mileage=db.Column(db.Integer)
    prod_year=db.Column(db.Integer)
    color=db.Column(db.String)
    photo=db.Column(db.String)
    location=db.Column(db.String)
    author = db.relationship('User', backref='author')

    def __init__(self,model_id,price,mileage,prod_year,color,location, user):
        self.model_id=model_id
        self.price=price
        self.mileage=mileage
        self.prod_year=prod_year
        self.color=color
        self.location=location
        self.author=user

    def set_photo(self, photo):
        self.photo = f"img/lots/{self.id}/1.png"

class PhotoModel(db.Model):
    __tablename__="photo"
    id = db.Column(db.Integer, primary_key=True)
    filename=db.Column(db.String)
    date=db.Column(db.Integer)
    advert=db.Column(db.String)
    photo=db.Column(db.String)

    def __init__(self,filename):
        self.filename=filename
        #self.date=

    def set_photo(self, photo):
        self.photo = f"img/lots/{self.id}/1.png"

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), unique=True )
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    lots_id = db.Column(db.Integer, db.ForeignKey(LotModel.id))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        hash = generate_password_hash(password)
        self.password = hash

    def check_password(self, password):
        return check_password_hash(self.password, password)
