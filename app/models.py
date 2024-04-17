from datetime import datetime
from datetime import timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))


class CartItem(db.Model):
    __tablename__ = "cart_item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float)
    title = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
