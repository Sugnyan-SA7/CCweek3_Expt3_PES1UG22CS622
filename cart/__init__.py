import json
from typing import List, Optional
from products import Product, get_product
from cart import dao

class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data: dict) -> 'Cart':
        return cls(
            id=data['id'], 
            username=data['username'], 
            contents=data['contents'], 
            cost=data['cost']
        )

def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []
    
    items = []
    for cart_detail in cart_details:
        # Safely parse contents instead of using eval
        contents = json.loads(cart_detail['contents'])
        items.extend(contents)
    
    # Use list comprehension and error handling
    return [
        get_product(item_id) 
        for item_id in items 
        if get_product(item_id) is not None
    ]

def add_to_cart(username: str, product_id: int) -> None:
    dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int) -> None:
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str) -> None:
    dao.delete_cart(username)