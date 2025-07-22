from flask import Flask, Blueprint, jsonify, request, abort
product_bp = Blueprint('product', __name__)

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 1200},
    {'id': 2, 'name': 'Shirt', 'category': 'clothing', 'price': 25},
    {'id': 3, 'name': 'Cookbook', 'category': 'books', 'price': 20},
    {'id': 4, 'name': 'Smartphone', 'category': 'electronics', 'price': 800},
    {'id': 5, 'name': 'Pants', 'category': 'clothing', 'price': 40}
]
next_product_id = 6

@product_bp.route('/product/products', methods=['GET'])
def get_products():
    return jsonify(products)

@product_bp.route('/product/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        abort(404)
    return jsonify(product)

@product_bp.route('/product/products', methods=['POST'])
def create_product():
    global next_product_id
    data = request.get_json()
    if 'name' not in data or 'description' not in data or 'price' not in data:
        abort(400, description="Missing required fields: name, description, price")
    new_product = {
        'id': next_product_id,
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(new_product)
    next_product_id += 1
    return jsonify(new_product), 201

@product_bp.route('/product/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        abort(404)
    data = request.get_json()
    product.update(data)  # Update existing product with new data
    return jsonify(product)

@product_bp.route('/product/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product_index = next((i for i, p in enumerate(products) if p['id'] == product_id), None)
    if product_index is None:
        abort(404)
    del products[product_index]
    return '', 204
