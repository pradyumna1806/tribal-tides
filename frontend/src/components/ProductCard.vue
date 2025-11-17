<template>
  <div class="product-card" @click="goToProduct">
    <div class="product-image">
      <img 
        :src="product.image_url || fallbackImage" 
        :alt="product.name"
        @error="handleImageError"
      />
      <div class="product-overlay">
        <button class="btn btn-primary" @click.stop="addToCart">Add to Cart</button>
      </div>
    </div>
    <div class="product-info">
      <h3>{{ product.name }}</h3>
      <p class="product-category">{{ product.category }}</p>
      <p class="product-price">₹{{ formatPrice(product.price) }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'ProductCard',
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const router = useRouter()
    const fallbackImage = 'https://drive.google.com/file/d/1sPG8oJ8JYDYQ11N2WuKRdyTY48-pigmj/view?usp=sharing'
    const imageError = ref(false)
    
    const formatPrice = (price) => {
      return new Intl.NumberFormat('en-IN').format(price.toFixed(0))
    }
    
    const handleImageError = (event) => {
      if (!imageError.value) {
        imageError.value = true
        event.target.src = fallbackImage
      }
    }
    
    const goToProduct = () => {
      router.push(`/product/${props.product.id}`)
    }
    
    const addToCart = () => {
      let cart = JSON.parse(localStorage.getItem('cart') || '[]')
      const existingItem = cart.find(item => item.product_id === props.product.id)
      
      if (existingItem) {
        existingItem.quantity += 1
      } else {
        cart.push({
          product_id: props.product.id,
          name: props.product.name,
          price: props.product.price,
          image_url: props.product.image_url,
          quantity: 1
        })
      }
      
      localStorage.setItem('cart', JSON.stringify(cart))
      
      // Emit event to update cart count
      window.dispatchEvent(new Event('cartUpdated'))
    }
    
    return {
      fallbackImage,
      imageError,
      formatPrice,
      handleImageError,
      goToProduct,
      addToCart
    }
  }
}
</script>

<style scoped>
.product-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid rgba(245, 230, 211, 0.5);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 28px rgba(201, 125, 96, 0.2);
  border-color: var(--terracotta);
}

.product-image {
  position: relative;
  width: 100%;
  padding-top: 100%; /* Square aspect ratio */
  overflow: hidden;
  background: linear-gradient(135deg, var(--sandy-beige) 0%, var(--turquoise) 100%);
  border-radius: 12px 12px 0 0;
}

.product-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
  border-radius: 12px 12px 0 0;
}

.product-card:hover .product-image img {
  transform: scale(1.08);
}

.product-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(61, 40, 23, 0.85), rgba(201, 125, 96, 0.75));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 12px 12px 0 0;
}

.product-card:hover .product-overlay {
  opacity: 1;
}

.product-overlay .btn {
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 600;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.product-info {
  padding: 1.25rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.product-info h3 {
  font-size: 17px;
  margin-bottom: 0.5rem;
  color: var(--deep-brown);
  line-height: 1.4;
  font-weight: 600;
  min-height: 2.4em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-category {
  font-size: 13px;
  color: var(--terracotta);
  text-transform: capitalize;
  margin-bottom: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.product-price {
  font-size: 22px;
  font-weight: 700;
  color: var(--turquoise);
  margin: auto 0 0 0;
  font-family: var(--font-sans);
}
</style>

