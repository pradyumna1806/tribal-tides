<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Tribal Tides</h1>
        <p class="hero-subtitle">Coastal & Tribal Fashion</p>
        <p class="hero-description">Discover unique pieces that blend coastal vibes with tribal heritage</p>
        <router-link to="/shop" class="btn btn-primary">Shop Now</router-link>
      </div>
    </section>

    <!-- New Arrivals -->
    <section class="section new-arrivals">
      <div class="container">
        <h2 class="section-title">New Arrivals</h2>
        <div class="products-grid" v-if="newArrivals.length > 0">
          <ProductCard v-for="product in newArrivals" :key="product.id" :product="product" />
        </div>
        <div v-else class="loading">Loading...</div>
      </div>
    </section>

    <!-- Featured Collections -->
    <section class="section featured-collections">
      <div class="container">
        <h2 class="section-title">Featured Collections</h2>
        <div class="collections-grid">
          <div class="collection-card" v-for="collection in collections" :key="collection.name">
            <div class="collection-image">
              <img :src="collection.image" :alt="collection.name" />
            </div>
            <div class="collection-info">
              <h3>{{ collection.name }}</h3>
              <router-link :to="collection.link" class="btn btn-outline">Explore</router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="section testimonials">
      <div class="container">
        <h2 class="section-title">What Our Customers Say</h2>
        <div class="testimonials-grid">
          <div class="testimonial-card" v-for="testimonial in testimonials" :key="testimonial.id">
            <p class="testimonial-text">"{{ testimonial.text }}"</p>
            <p class="testimonial-author">— {{ testimonial.author }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ProductCard from '../components/ProductCard.vue'

export default {
  name: 'Home',
  components: {
    ProductCard
  },
  setup() {
    const newArrivals = ref([])
    const collections = ref([
      {
        name: 'Coastal Collection',
        image: 'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=500',
        link: '/shop?category=clothing'
      },
      {
        name: 'Tribal Jewelry',
        image: 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500',
        link: '/shop?category=jewelry'
      },
      {
        name: 'Beach Footwear',
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500',
        link: '/shop?category=footwear'
      }
    ])
    const testimonials = ref([
      {
        id: 1,
        text: 'Absolutely love my new maxi dress! The quality is amazing and the design is unique.',
        author: 'Sarah M.'
      },
      {
        id: 2,
        text: 'The jewelry pieces are stunning. I get compliments every time I wear them.',
        author: 'Jessica L.'
      },
      {
        id: 3,
        text: 'Perfect blend of comfort and style. Tribal Tides has become my go-to brand!',
        author: 'Emily R.'
      }
    ])

    onMounted(async () => {
      try {
        const response = await axios.get('/api/products')
        // Get first 4 products as new arrivals
        newArrivals.value = response.data.slice(0, 4)
      } catch (error) {
        console.error('Error fetching products:', error)
      }
    })

    return {
      newArrivals,
      collections,
      testimonials
    }
  }
}
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, var(--sandy-beige) 0%, var(--turquoise) 100%);
  padding: 8rem 2rem;
  text-align: center;
  color: var(--deep-brown);
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--terracotta);
}

.hero-description {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.section {
  padding: 4rem 0;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: var(--deep-brown);
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 2rem;
}

.collections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.collection-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.collection-card:hover {
  transform: translateY(-5px);
}

.collection-image {
  width: 100%;
  height: 300px;
  overflow: hidden;
}

.collection-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.collection-info {
  padding: 1.5rem;
  text-align: center;
}

.collection-info h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.testimonial-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.testimonial-text {
  font-size: 1.1rem;
  font-style: italic;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.testimonial-author {
  font-weight: 600;
  color: var(--terracotta);
}

.loading {
  text-align: center;
  padding: 2rem;
  color: var(--terracotta);
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
  }
  
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
}
</style>

