from flask import json


def test_create_cart(client):
    response = client.post("/api/cart")
    assert response.status_code == 200
    assert json.loads(response.data) == {"id": 1}


def test_get_cart(client):
    response = client.get("/api/cart/1")
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "id": 1,
        "cart_items": [],
        "subtotal": "0",
        "total_items": 0,
    }


def test_add_item(client):
    response = client.post(
        "/api/cart/1/item",
        data=json.dumps({"product_id": "1", "quantity": 1}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "id": 1,
    }


def test_update_item(client):
    response = client.patch(
        "/api/cart/1/item/1",
        data=json.dumps({"quantity": 4}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Item quantity updated"}


def test_remove_item(client):
    response = client.delete("/api/cart/1/item/1")
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Item removed from cart"}


def test_remove_item_not_found(client):
    response = client.delete("/api/cart/1/item/5")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Item not found in cart"}


def test_update_item_not_found(client):
    response = client.patch(
        "/api/cart/1/item/5",
        data=json.dumps({"quantity": 4}),
        content_type="application/json",
    )
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Item not found in cart"}


def test_get_cart_not_found(client):
    response = client.get("/api/cart/5")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Cart not found"}
