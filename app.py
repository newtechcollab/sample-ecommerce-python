from flask import Flask
from catalog.service import catalog_bp
from product.service import product_bp

app = Flask(__name__)
app.register_blueprint(catalog_bp)
app.register_blueprint(product_bp)

@app.route('/')
def index():
    return "This is an eCommerce app"

if __name__ == '__main__':
    app.run(debug=True)
