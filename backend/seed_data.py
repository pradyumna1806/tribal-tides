from app import app, db
from models import Product

PRODUCT_CATALOG = [
    {
        "name": "Kaftan Dress",
        "category": "Women's Wear",
        "price": 2499.00,
        "description": "Flowing kaftan with modern tribal embroidery and an easy coastal fit.",
        "material": "Breathable Linen",
        "sizes": "XS,S,M,L,XL",
        "image_file": "kaftan_dress.jpg"
    },
    {
        "name": "Crochet Top",
        "category": "Women's Wear",
        "price": 1999.00,
        "description": "Hand-knotted crochet top inspired by shoreline textures.",
        "material": "Cotton Yarn",
        "sizes": "XS,S,M,L",
        "image_file": "crochet_top.jpg"
    },
    {
        "name": "Maxi Dress",
        "category": "Women's Wear",
        "price": 2899.00,
        "description": "Resort-ready maxi dress with wave motifs and a relaxed silhouette.",
        "material": "Cotton & Viscose",
        "sizes": "S,M,L,XL",
        "image_file": "maxi_dress.jpg"
    },
    {
        "name": "Linen Shirt",
        "category": "Men's Wear",
        "price": 2199.00,
        "description": "Lightweight linen shirt with subtle tribal piping on the placket.",
        "material": "100% Linen",
        "sizes": "S,M,L,XL,XXL",
        "image_file": "linen_shirt.jpg"
    },
    {
        "name": "Resort Shorts",
        "category": "Men's Wear",
        "price": 1599.00,
        "description": "Relaxed-fit resort shorts with woven belt detail and coconut buttons.",
        "material": "Linen & Cotton",
        "sizes": "S,M,L,XL,XXL",
        "image_file": "resort_shorts.jpg"
    },
    {
        "name": "Boho Bag",
        "category": "Accessories",
        "price": 1899.00,
        "description": "Fringed boho bag with beadwork and a roomy interior for beach days.",
        "material": "Woven Jute & Leather",
        "sizes": "One Size",
        "image_file": "boho_bag.jpg"
    },
    {
        "name": "Beaded Anklet",
        "category": "Accessories",
        "price": 799.00,
        "description": "Stackable anklet featuring seed beads and shell charms.",
        "material": "Glass Beads & Shell",
        "sizes": "Adjustable",
        "image_file": "beaded_anklet.jpg"
    },
    {
        "name": "Woven Sandals",
        "category": "Footwear",
        "price": 2299.00,
        "description": "Handwoven sandals with cushioned footbeds for all-day comfort.",
        "material": "Leather & Raffia",
        "sizes": "5,6,7,8,9,10",
        "image_file": "woven_sandals.jpg"
    },
    {
        "name": "Beaded Flats",
        "category": "Footwear",
        "price": 1999.00,
        "description": "Slide-on flats detailed with coral-inspired beadwork.",
        "material": "Vegan Leather",
        "sizes": "5,6,7,8,9,10",
        "image_file": "beaded_flats.jpg"
    },
    {
        "name": "Shell Necklace",
        "category": "Jewelry / Chains",
        "price": 1299.00,
        "description": "Layered shell necklace with hammered metal charms.",
        "material": "Shell & Brass",
        "sizes": "One Size",
        "image_file": "shell_necklace.jpg"
    },
    {
        "name": "Tribal Earrings",
        "category": "Jewelry / Chains",
        "price": 999.00,
        "description": "Statement earrings with etched tribal discs and bead drops.",
        "material": "Brass & Glass",
        "sizes": "One Size",
        "image_file": "tribal_earrings.jpg"
    },
    {
        "name": "Coastal Nude Tint",
        "category": "Beauty (Lip Shades)",
        "price": 649.00,
        "description": "Moisturizing lip tint that delivers a soft nude sheen.",
        "material": "Aloe, Coconut Oil",
        "sizes": "One Size",
        "image_file": "coastal_nude_tint.jpg"
    },
    {
        "name": "Coral Lip Tint",
        "category": "Beauty (Lip Shades)",
        "price": 599.00,
        "description": "Buildable coral tint with SPF protection for beach days.",
        "material": "Shea Butter, Mineral Pigments",
        "sizes": "One Size",
        "image_file": "coral_lip_tint.jpg"
    },
    {
        "name": "Neo Tribal Minimal",
        "category": "Tattoo Styles (Temporary)",
        "price": 349.00,
        "description": "Minimalist temporary tattoo set with crisp tribal lines.",
        "material": "Non-toxic Temporary Ink",
        "sizes": "Small, Medium",
        "image_file": "neo_tribal_minimal.jpg"
    },
    {
        "name": "Wave Stripe Tattoo",
        "category": "Tattoo Styles (Temporary)",
        "price": 329.00,
        "description": "Wave stripe temporary tattoo inspired by tidal patterns.",
        "material": "Non-toxic Temporary Ink",
        "sizes": "Medium, Large",
        "image_file": "wave_stripe_tattoo.jpg"
    },
]

def image_path(filename: str) -> str:
    return f"/static/images/products/{filename}"


def seed_database():
    """Seed the database with curated category-based products."""
    with app.app_context():
        Product.query.delete()

        products = [
            Product(
                name=data["name"],
                category=data["category"],
                price=data["price"],
                description=data["description"],
                image_url=image_path(data["image_file"]),
                material=data["material"],
                sizes=data["sizes"]
            )
            for data in PRODUCT_CATALOG
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()
        print(f"Seeded {len(products)} products successfully!")


if __name__ == '__main__':
    seed_database()
