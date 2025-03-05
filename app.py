from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data
products = [
    {"id": 1, "name": "Cyber Hoodie", "price": 29.99, "image": "static/hoodie.jpg"},
    {"id": 2, "name": "Bug Bounty Shirt", "price": 19.99, "image": "static/shirt.jpg"},
    {"id": 3, "name": "Pen-Testing Cap", "price": 14.99, "image": "static/cap.jpg"},
]

@app.route('/')
def home():
    return render_template("index.html", products=products)

@app.route('/shop')
def shop():
    return render_template("shop.html", products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template("product.html", product=product) if product else "Product not found"

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)
