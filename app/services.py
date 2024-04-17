from .models import Cart, CartItem, db
from decimal import Decimal


def get_cart(cart_id):
    cart = Cart.query.filter_by(id=cart_id).first()
    if cart:
        cart_items = (
            CartItem.query.filter_by(cart_id=cart_id).order_by(CartItem.id.asc()).all()
        )
        list_cart_items = [
            {
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "image_url": item.image_url,
                "title": item.title,
                "price": Decimal(item.price).quantize(Decimal("0.00")),
                "total_price": Decimal(item.price * item.quantity).quantize(
                    Decimal("0.00")
                ),
            }
            for item in cart_items
        ]

        subtotal = Decimal(0)
        total_items = 0
        for item in list_cart_items:
            subtotal += Decimal(item["price"]) * item["quantity"]
            total_items = sum([item["quantity"] for item in list_cart_items])

        return {
            "id": cart.id,
            "cart_items": list_cart_items,
            "subtotal": subtotal,
            "total_items": total_items,
        }
    return cart or {"error": "Cart not found"}


def create_cart():
    cart = Cart()
    db.session.add(cart)
    db.session.commit()
    return {"id": cart.id}


def add_item_to_cart(cart_id, data):
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    image_url = data.get("image_url")
    price = data.get("price")
    title = data.get("title")
    verify_item = CartItem.query.filter_by(
        cart_id=cart_id, product_id=product_id
    ).first()

    if verify_item:
        verify_item.quantity += int(quantity)
        db.session.commit()
        return {"id": verify_item.id}

    cart_item = CartItem(
        cart_id=cart_id,
        product_id=product_id,
        quantity=quantity,
        image_url=image_url,
        price=price,
        title=title,
    )
    db.session.add(cart_item)
    db.session.commit()
    return {"id": cart_item.id}


def remove_item_from_cart(cart_id, product_id):
    cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    print(cart_item)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return {"message": "Item removed from cart"}
    return {"error": "Item not found in cart"}


def update_item_quantity(cart_id, product_id, quantity):
    cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity = quantity
        db.session.commit()
        return {"message": "Item quantity updated"}
    return {"error": "Item not found in cart"}
