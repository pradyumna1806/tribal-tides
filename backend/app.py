from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models import db, Product, Order, OrderItem, Booking
import os
from datetime import datetime

# Configure Flask to serve the built Vue app
app = Flask(__name__, static_folder="dist", static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

STATIC_IMAGES_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static', 'images'))

# Enable CORS - allow all origins in production, specific origins in dev
# In production (Render), we serve from the same domain, so CORS is less critical
# But we keep it enabled for API flexibility
if os.environ.get('RENDER'):
    CORS(app)  # Allow all origins in production
else:
    CORS(app, origins=["http://localhost:5173", "http://localhost:3000"])

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# ========== PRODUCT ROUTES ==========

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products with optional filters"""
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    material = request.args.get('material')
    
    query = Product.query
    
    if category:
        query = query.filter(Product.category == category)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if material:
        query = query.filter(Product.material.like(f'%{material}%'))
    
    products = query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price,
        'description': p.description,
        'image_url': p.image_url,
        'material': p.material,
        'sizes': p.sizes
    } for p in products])

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a single product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'description': product.description,
        'image_url': product.image_url,
        'material': product.material,
        'sizes': product.sizes
    })

# ========== CART ROUTES ==========

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    """Add item to cart (stored in session or localStorage on frontend)"""
    data = request.json
    # For simplicity, cart is managed on frontend
    # This endpoint can be used for validation
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify({
        'success': True,
        'product': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url
        },
        'quantity': quantity
    })

@app.route('/api/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    """Remove item from cart"""
    # Cart managed on frontend, this is for API consistency
    return jsonify({'success': True, 'message': 'Item removed'})

# ========== ORDER ROUTES ==========

@app.route('/api/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    data = request.json
    
    try:
        order = Order(
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            address=data['address'],
            total_price=data['total_price']
        )
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Add order items
        for item in data['items']:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product_id'],
                quantity=item['quantity']
            )
            db.session.add(order_item)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'order_id': order.id,
            'message': 'Order created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# ========== BOOKING ROUTES ==========

@app.route('/api/book-tattoo', methods=['POST'])
def book_tattoo():
    """Create a tattoo booking"""
    data = request.json
    
    try:
        booking = Booking(
            name=data['name'],
            date=data['date'],
            time=data['time'],
            style=data['style']
        )
        db.session.add(booking)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'booking_id': booking.id,
            'message': 'Booking created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """Get all bookings (for admin)"""
    bookings = Booking.query.all()
    return jsonify([{
        'id': b.id,
        'name': b.name,
        'date': b.date,
        'time': b.time,
        'style': b.style,
        'created_at': b.created_at.isoformat() if b.created_at else None
    } for b in bookings])

# ========== CATEGORIES ==========

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all product categories"""
    categories = db.session.query(Product.category).distinct().all()
    return jsonify([cat[0] for cat in categories])

@app.route('/static/images/<path:filename>')
def serve_static_images(filename):
    """Serve placeholder product and category images."""
    if not os.path.isdir(STATIC_IMAGES_ROOT):
        return jsonify({'error': 'Static images directory missing'}), 404
    return send_from_directory(STATIC_IMAGES_ROOT, filename)

# Serve Vue app - must be after all API routes
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_vue(path):
    """Serve the Vue.js frontend"""
    # Ensure static_folder exists
    if not os.path.exists(app.static_folder):
        return jsonify({"error": "Frontend not built. Please run 'npm run build' in the frontend directory."}), 503
    
    # Serve static files if they exist
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Fallback to index.html for Vue Router
    index_path = os.path.join(app.static_folder, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(app.static_folder, "index.html")
    
    return jsonify({"error": "Frontend not found. Please build the frontend first."}), 503

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

