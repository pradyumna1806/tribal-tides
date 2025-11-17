<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import ProductCard from '../components/ProductCard.vue'

const CATEGORY_SOURCE = [
  {
    name: "Women's Wear",
    image: '/static/images/categories/womens_wear.jpg',
    description: 'Kaftans, maxi dresses, and breezy layers for shoreline sunsets.'
  },
  {
    name: "Men's Wear",
    image: '/static/images/categories/mens_wear.jpg',
    description: 'Relaxed shirts and shorts tailored for resort-ready comfort.'
  },
  {
    name: 'Accessories',
    image: '/static/images/categories/accessories.jpg',
    description: 'Bags, belts, and anklets crafted with shells, beads, and raffia.'
  },
  {
    name: 'Footwear',
    image: '/static/images/categories/footwear.jpg',
    description: 'Hand-detailed flats and sandals that echo tidal textures.'
  },
  {
    name: 'Jewelry / Chains',
    image: '/static/images/categories/jewelry_chains.jpg',
    description: 'Layered shells, polished metals, and tribal-inspired silhouettes.'
  },
  {
    name: 'Beauty (Lip Shades)',
    image: '/static/images/categories/beauty_lip_shades.jpg',
    description: 'Hydrating tints in coral palettes for sunlit glow.'
  },
  {
    name: 'Tattoo Styles (Temporary)',
    image: '/static/images/categories/tattoo_styles_temporary.jpg',
    description: 'Skin-safe temporary art featuring minimalist tribal lines.'
  }
]

export default {
  name: 'Home',
  components: {
    ProductCard
  },
  setup() {
    const router = useRouter()
    const newArrivals = ref([])
    const categoryCards = ref(
      CATEGORY_SOURCE.map(category => ({
        ...category,
        link: `/shop?category=${encodeURIComponent(category.name)}`
      }))
    )
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

    const goToCategory = (categoryName) => {
      router.push({ path: '/shop', query: { category: categoryName } })
    }

    onMounted(async () => {
      try {
        const response = await axios.get('/api/products')
        newArrivals.value = response.data.slice(0, 4)
      } catch (error) {
        console.error('Error fetching products:', error)
      }
    })

    return {
      newArrivals,
      categoryCards,
      testimonials,
      goToCategory
    }
  }
}
</script>

<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Tribal Tides</h1>
        <p class="hero-subtitle">Coastal & Tribal Fashion</p>
        <p class="hero-description">Discover unique pieces that blend coastal vibes with tribal heritage</p>
        <router-link to="/shop" class="btn btn-primary">Shop Now</router-link>
      </div>
    </section>

    <section class="section categories-section">
      <div class="container">
        <h2 class="section-title">Shop by Category</h2>
        <div class="categories-grid">
          <div
            class="category-card"
            v-for="category in categoryCards"
            :key="category.name"
            role="button"
            tabindex="0"
            @click="goToCategory(category.name)"
            @keyup.enter.prevent="goToCategory(category.name)"
            @keyup.space.prevent="goToCategory(category.name)"
          >
            <div class="category-image">
              <img :src="category.image" :alt="category.name" />
            </div>
            <div class="category-info">
              <h3>{{ category.name }}</h3>
              <p>{{ category.description }}</p>
              <router-link :to="category.link" class="btn btn-outline">View</router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section new-arrivals">
      <div class="container">
        <h2 class="section-title">New Arrivals</h2>
        <div class="products-grid" v-if="newArrivals.length > 0">
          <ProductCard v-for="product in newArrivals" :key="product.id" :product="product" />
        </div>
        <div v-else class="loading">Loading...</div>
      </div>
    </section>

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

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 2rem;
}

.category-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid rgba(61, 40, 23, 0.08);
}

.category-card:focus-visible {
  outline: 3px solid var(--turquoise);
}

.category-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 32px rgba(34, 50, 84, 0.15);
}

.category-image {
  width: 100%;
  padding-top: 65%;
  position: relative;
  overflow: hidden;
}

.category-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.category-card:hover .category-image img {
  transform: scale(1.05);
}

.category-info {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.category-info h3 {
  margin: 0;
  font-size: 1.4rem;
  color: var(--deep-brown);
}

.category-info p {
  color: rgba(61, 40, 23, 0.8);
  min-height: 3.5rem;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 2.5rem;
  padding: 1rem 0;
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

  .categories-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }

  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
}
</style>
