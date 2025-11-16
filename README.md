# Tribal Tides - E-Commerce Website

A full-stack e-commerce website for Tribal Tides, a brand that sells clothing, accessories, footwear, jewelry, and offers temporary tattoo services. Built with a coastal + tribal aesthetic.

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: Vue 3 + Vite
- **Database**: SQLite3
- **Styling**: CSS with custom properties
- **API Communication**: REST API (JSON)

## Project Structure

```
TRIBAL_TIDES/
├── backend/
│   ├── app.py              # Flask application and API routes
│   ├── models.py           # SQLAlchemy database models
│   ├── requirements.txt    # Python dependencies
│   ├── seed_data.py        # Database seeding script
│   ├── database.db         # SQLite database (created on first run)
│   └── dist/               # Built Vue frontend (created by npm run build)
│
├── frontend/
│   ├── index.html          # HTML entry point
│   ├── package.json        # Node.js dependencies
│   ├── vite.config.js      # Vite configuration
│   └── src/
│       ├── main.js         # Vue app entry point
│       ├── App.vue         # Root component
│       ├── assets/
│       │   └── style.css   # Global styles and CSS variables
│       ├── components/
│       │   ├── NavBar.vue
│       │   ├── Footer.vue
│       │   └── ProductCard.vue
│       └── views/
│           ├── Home.vue
│           ├── Shop.vue
│           ├── ProductDetail.vue
│           ├── Cart.vue
│           ├── Checkout.vue
│           ├── BookTattoo.vue
│           ├── About.vue
│           └── Contact.vue
│
├── render.yaml             # Render.com deployment configuration
├── DEPLOYMENT_CHECKLIST.md  # Step-by-step deployment guide
└── README.md
```

## Features

### Pages
- **Homepage**: Hero section, new arrivals, featured collections, testimonials
- **Shop**: Product listing with filters (category, price, material)
- **Product Detail**: Image gallery, product info, add to cart, recommended products
- **Cart**: Shopping cart with quantity controls
- **Checkout**: Order form and summary
- **Book Tattoo**: Temporary tattoo booking form
- **About**: Brand story and values
- **Contact**: Contact form and information

### Backend API Endpoints
- `GET /api/products` - Get all products (with optional filters)
- `GET /api/products/<id>` - Get single product
- `POST /api/cart` - Add item to cart (validation)
- `DELETE /api/cart/<item_id>` - Remove item from cart
- `POST /api/orders` - Create new order
- `POST /api/book-tattoo` - Create tattoo booking
- `GET /api/categories` - Get all product categories
- `GET /api/bookings` - Get all bookings (admin)

## Setup Instructions

### Prerequisites
- Python 3.8+ installed
- Node.js 16+ and npm installed

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database and seed with sample data:
```bash
python seed_data.py
```

5. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the Vite development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

### Production Build

To build the frontend for production:
```bash
cd frontend
npm run build
```

The built files will be in `backend/dist/` (configured in `vite.config.js`)

**Note**: After building, Flask will serve the frontend from `backend/dist/` when running in production mode.

## Database Schema

### Products Table
- `id` (Integer, Primary Key)
- `name` (String)
- `category` (String) - clothing, accessories, footwear, jewelry
- `price` (Float)
- `description` (Text)
- `image_url` (String)
- `material` (String)
- `sizes` (String) - comma-separated sizes

### Orders Table
- `id` (Integer, Primary Key)
- `customer_name` (String)
- `customer_email` (String)
- `address` (Text)
- `total_price` (Float)
- `created_at` (DateTime)

### Order Items Table
- `id` (Integer, Primary Key)
- `order_id` (Integer, Foreign Key)
- `product_id` (Integer, Foreign Key)
- `quantity` (Integer)

### Bookings Table
- `id` (Integer, Primary Key)
- `name` (String)
- `date` (String) - YYYY-MM-DD format
- `time` (String) - HH:MM format
- `style` (String)
- `created_at` (DateTime)

## Design Theme

### Colors
- **Sandy Beige**: `#F5E6D3`
- **Terracotta**: `#C97D60`
- **Turquoise**: `#4A9B8E`
- **Deep Brown**: `#3D2817`
- **Cream**: `#FAF7F2`

### Typography
- **Serif**: Playfair Display (for headings)
- **Sans-serif**: Inter (for body text)

## Cart Management

The shopping cart is stored in the browser's `localStorage`. Cart updates trigger a `cartUpdated` event that components listen to for reactive updates.

## Development Notes

- CORS is enabled for `http://localhost:5173` and `http://localhost:3000`
- The Vite dev server proxies `/api` requests to `http://localhost:5000`
- Product images use placeholder URLs from Unsplash
- The database is automatically created on first run

## Deployment to Render.com

This project is configured for deployment on Render.com with a single public URL serving both frontend and backend.

### Prerequisites
- GitHub account
- Render.com account (free tier available)

### Deployment Steps

1. **Build the frontend** (before pushing to GitHub):
   ```bash
   cd frontend
   npm install
   npm run build
   ```
   This creates the `backend/dist/` folder with the built Vue app.

2. **Commit and push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

3. **Deploy on Render.com**:
   - Go to [Render.com](https://render.com) and sign in
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: `tribal-tides` (or your preferred name)
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

4. **Initialize the database** (after first deployment):
   - Once deployed, you can SSH into the service or use Render's shell
   - Run: `python seed_data.py` to populate the database
   - Alternatively, the database will auto-create on first API call

5. **Access your site**:
   - Render will provide a public URL (e.g., `https://tribal-tides.onrender.com`)
   - The site will serve both frontend and API from this single URL

### Using render.yaml (Alternative Method)

If you prefer using the `render.yaml` file:
- Push `render.yaml` to your repository root
- In Render dashboard, select "Apply Render Configuration"
- Render will automatically detect and use the configuration

### Important Notes for Production

- **Database**: SQLite database is created automatically in the `backend/` directory
- **Static Files**: The built Vue app must be in `backend/dist/` before deployment
- **Environment Variables**: No environment variables required for basic deployment
- **CORS**: CORS is configured to work with the single-domain setup
- **Port**: Render automatically sets the PORT environment variable; Gunicorn uses it automatically

### Updating After Deployment

1. Make changes to your code
2. Build the frontend: `cd frontend && npm run build`
3. Commit and push: `git add . && git commit -m "Update" && git push`
4. Render will automatically redeploy

## Troubleshooting

### Backend Issues
- Ensure Flask is installed: `pip install Flask Flask-SQLAlchemy Flask-CORS gunicorn`
- If database errors occur, delete `database.db` and run `seed_data.py` again
- Check that port 5000 is not in use (local development)
- For Render: Ensure `gunicorn` is in `requirements.txt`

### Frontend Issues
- Clear `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Ensure the backend is running before starting the frontend (local dev)
- Check browser console for CORS errors
- **For production**: Make sure `npm run build` is run before deploying

### Deployment Issues
- Ensure `backend/dist/` exists before deploying
- Check Render logs for build/start command errors
- Verify `rootDir` is set to `backend` in Render dashboard
- Ensure all dependencies are in `requirements.txt`

## Future Enhancements

- User authentication and accounts
- Payment gateway integration
- Product reviews and ratings
- Admin panel for managing products and orders
- Email notifications for orders
- Image upload functionality
- Search functionality
- Wishlist feature

## License

This project is created for educational purposes.

## Contact

For questions or support, please contact: hello@tribaltides.com

