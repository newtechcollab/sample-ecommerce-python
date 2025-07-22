from flask import Flask, Blueprint, jsonify, request
catalog_bp = Blueprint('catalog', __name__)

app = Flask(__name__)

# Sample data (replace with database integration in a real system)
categories = {
    "electronics": ["laptop", "smartphone", "tablet"],
    "clothing": ["shirt", "pants", "dress"],
    "books": ["fiction", "non-fiction", "cookbook"]
}

products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 1200},
    {'id': 2, 'name': 'Shirt', 'category': 'clothing', 'price': 25},
    {'id': 3, 'name': 'Cookbook', 'category': 'books', 'price': 20},
    {'id': 4, 'name': 'Smartphone', 'category': 'electronics', 'price': 800},
    {'id': 5, 'name': 'Pants', 'category': 'clothing', 'price': 40}
]


@catalog_bp.route('/catalog/categories', methods=['GET'])
def get_categories():
    return jsonify(list(categories.keys()))


@catalog_bp.route('/catalog/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    if category:
        filtered_products = [p for p in products if p['category'] == category]
        return jsonify(filtered_products)
    else:
        return jsonify(products)


@catalog_bp.route('/catalog/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    #if product is None:
    #    return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)
