from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Reptiles(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(50))
    scientific_name = db.Column(db.String(50))
    conservation_status = db.Column(db.String(50))
    native_habitat = db.Column(db.String(50))
    fun_fact = db.Column(db.Text)
