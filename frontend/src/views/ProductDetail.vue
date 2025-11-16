<template>
  <div class="product-detail">
    <div class="container" v-if="product">
      <div class="product-detail-content">
        <!-- Image Gallery -->
        <div class="product-images">
          <div class="main-image">
            <img :src="product.image_url || '/placeholder.jpg'" :alt="product.name" />
          </div>
        </div>
        
        <!-- Product Info -->
        <div class="product-info">
          <h1>{{ product.name }}</h1>
          <p class="product-category">{{ product.category }}</p>
          <p class="product-price">${{ product.price.toFixed(2) }}</p>
          
          <div class="product-description">
            <h3>Description</h3>
            <p>{{ product.description }}</p>
          </div>
          
          <div class="product-details">
            <div v-if="product.material">
              <strong>Material:</strong> {{ product.material }}
            </div>
            <div v-if="product.sizes">
              <strong>Available Sizes:</strong> {{ product.sizes }}
            </div>
          </div>
          
          <div class="product-actions">
            <select v-model="selectedSize" class="size-select">
              <option value="">Select Size</option>
              <option v-for="size in availableSizes" :key="size" :value="size">
                {{ size }}
              </option>
            </select>
            
            <div class="quantity-control">
              <label>Quantity:</label>
              <button @click="decreaseQuantity">-</button>
              <span>{{ quantity }}</span>
              <button @click="increaseQuantity">+</button>
            </div>
            
            <button @click="addToCart" class="btn btn-primary btn-large">
              Add to Cart
            </button>
          </div>
        </div>
      </div>
      
      <!-- Recommended Products -->
      <section class="recommended">
        <h2>You May Also Like</h2>
        <div class="products-grid" v-if="recommendedProducts.length > 0">
          <ProductCard 
            v-for="rec in recommendedProducts" 
            :key="rec.id" 
            :product="rec" 
          />
        </div>
      </section>
    </div>
    <div v-else class="loading">
      <p>Loading product...</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import ProductCard from '../components/ProductCard.vue'

export default {
  name: 'ProductDetail',
  components: {
    ProductCard
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const product = ref(null)
    const recommendedProducts = ref([])
    const selectedSize = ref('')
    const quantity = ref(1)

    const availableSizes = computed(() => {
      if (!product.value || !product.value.sizes) return []
      return product.value.sizes.split(',').map(s => s.trim())
    })

    const increaseQuantity = () => {
      quantity.value++
    }

    const decreaseQuantity = () => {
      if (quantity.value > 1) {
        quantity.value--
      }
    }

    const addToCart = () => {
      if (!product.value) return

      let cart = JSON.parse(localStorage.getItem('cart') || '[]')
      const existingItem = cart.find(item => 
        item.product_id === product.value.id && item.size === selectedSize.value
      )

      if (existingItem) {
        existingItem.quantity += quantity.value
      } else {
        cart.push({
          product_id: product.value.id,
          name: product.value.name,
          price: product.value.price,
          image_url: product.value.image_url,
          quantity: quantity.value,
          size: selectedSize.value
        })
      }

      localStorage.setItem('cart', JSON.stringify(cart))
      window.dispatchEvent(new Event('cartUpdated'))
      
      alert('Added to cart!')
    }

    onMounted(async () => {
      try {
        const productId = route.params.id
        const response = await axios.get(`/api/products/${productId}`)
        product.value = response.data

        // Fetch recommended products (same category, different product)
        const allProducts = await axios.get('/api/products')
        recommendedProducts.value = allProducts.data
          .filter(p => p.category === product.value.category && p.id !== product.value.id)
          .slice(0, 4)
      } catch (error) {
        console.error('Error fetching product:', error)
        router.push('/shop')
      }
    })

    return {
      product,
      recommendedProducts,
      selectedSize,
      quantity,
      availableSizes,
      increaseQuantity,
      decreaseQuantity,
      addToCart
    }
  }
}
</script>

<style scoped>
.product-detail {
  padding: 2rem 0;
  min-height: 60vh;
}

.product-detail-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.product-images {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.main-image {
  width: 100%;
  aspect-ratio: 1;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background-color: var(--sandy-beige);
}

.main-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-info h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: var(--deep-brown);
}

.product-category {
  font-size: 1.1rem;
  color: var(--terracotta);
  text-transform: capitalize;
  margin-bottom: 1rem;
}

.product-price {
  font-size: 2rem;
  font-weight: 600;
  color: var(--turquoise);
  margin-bottom: 2rem;
}

.product-description {
  margin-bottom: 2rem;
}

.product-description h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.product-details {
  margin-bottom: 2rem;
  padding: 1rem;
  background: var(--sandy-beige);
  border-radius: 4px;
}

.product-details div {
  margin-bottom: 0.5rem;
}

.product-actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.size-select {
  padding: 12px;
  border: 2px solid var(--deep-brown);
  border-radius: 4px;
  font-size: 16px;
  background: white;
}

.quantity-control {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.quantity-control button {
  width: 40px;
  height: 40px;
  border: 2px solid var(--deep-brown);
  background: white;
  border-radius: 4px;
  font-size: 20px;
  font-weight: 600;
}

.quantity-control button:hover {
  background: var(--sandy-beige);
}

.quantity-control span {
  font-size: 18px;
  font-weight: 600;
  min-width: 30px;
  text-align: center;
}

.btn-large {
  padding: 16px 32px;
  font-size: 18px;
}

.recommended {
  margin-top: 4rem;
  padding-top: 3rem;
  border-top: 2px solid var(--sandy-beige);
}

.recommended h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 2rem;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 2rem;
}

.loading {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--terracotta);
  font-size: 1.2rem;
}

@media (max-width: 968px) {
  .product-detail-content {
    grid-template-columns: 1fr;
  }
  
  .product-images {
    position: static;
  }
}
</style>

