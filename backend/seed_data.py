from app import app, db
from models import Product

def seed_database():
    """Seed the database with sample products"""
    with app.app_context():
        # Clear existing products
        Product.query.delete()
        
        products = [
            # Clothing
            Product(
                name="Coastal Breeze Maxi Dress",
                category="clothing",
                price=89.99,
                description="Flowing maxi dress with tribal-inspired patterns. Perfect for beach days or evening strolls.",
                image_url="https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500",
                material="Cotton, Linen blend",
                sizes="XS,S,M,L,XL"
            ),
            Product(
                name="Tribal Print Tunic",
                category="clothing",
                price=59.99,
                description="Comfortable tunic with geometric tribal patterns. Versatile for any occasion.",
                image_url="https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500",
                material="100% Cotton",
                sizes="S,M,L,XL"
            ),
            Product(
                name="Ocean Waves Tank Top",
                category="clothing",
                price=34.99,
                description="Lightweight tank top with wave-inspired design. Perfect for warm weather.",
                image_url="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500",
                material="Organic Cotton",
                sizes="XS,S,M,L"
            ),
            
            # Accessories
            Product(
                name="Seashell Statement Necklace",
                category="accessories",
                price=45.99,
                description="Handcrafted necklace featuring natural seashells and turquoise beads.",
                image_url="https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500",
                material="Seashells, Turquoise, Silver",
                sizes="One Size"
            ),
            Product(
                name="Tribal Pattern Scarf",
                category="accessories",
                price=29.99,
                description="Silk scarf with bold tribal geometric patterns. Perfect accessory for any outfit.",
                image_url="https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=500",
                material="100% Silk",
                sizes="One Size"
            ),
            Product(
                name="Coastal Tote Bag",
                category="accessories",
                price=49.99,
                description="Spacious tote bag with tribal embroidery. Perfect for beach days or shopping.",
                image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
                material="Canvas, Leather accents",
                sizes="One Size"
            ),
            
            # Footwear
            Product(
                name="Beach Sandals",
                category="footwear",
                price=64.99,
                description="Comfortable leather sandals with tribal-inspired straps. Perfect for coastal adventures.",
                image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
                material="Genuine Leather",
                sizes="6,7,8,9,10,11"
            ),
            Product(
                name="Tribal Moccasins",
                category="footwear",
                price=79.99,
                description="Handcrafted moccasins with traditional patterns. Comfortable and stylish.",
                image_url="https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500",
                material="Suede Leather",
                sizes="6,7,8,9,10,11"
            ),
            
            # Jewelry
            Product(
                name="Turquoise Drop Earrings",
                category="jewelry",
                price=39.99,
                description="Elegant drop earrings featuring turquoise stones and silver details.",
                image_url="https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500",
                material="Turquoise, Sterling Silver",
                sizes="One Size"
            ),
            Product(
                name="Ocean Wave Bracelet",
                category="jewelry",
                price=32.99,
                description="Delicate bracelet with wave-inspired design. Adjustable sizing.",
                image_url="https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=500",
                material="Sterling Silver",
                sizes="Adjustable"
            ),
            Product(
                name="Tribal Ring Set",
                category="jewelry",
                price=54.99,
                description="Set of three stacking rings with geometric tribal patterns.",
                image_url="https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=500",
                material="Sterling Silver",
                sizes="6,7,8,9"
            ),
            Product(
                name="Coastal Anklet",
                category="jewelry",
                price=24.99,
                description="Dainty anklet with seashell charms. Perfect for beach vibes.",
                image_url="https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=500",
                material="Sterling Silver, Seashells",
                sizes="Adjustable"
            ),
        ]
        
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        print(f"Seeded {len(products)} products successfully!")

if __name__ == '__main__':
    seed_database()

