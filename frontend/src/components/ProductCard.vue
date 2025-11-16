<template>
  <div class="product-card" @click="goToProduct">
    <div class="product-image">
      <img :src="product.image_url || '/placeholder.jpg'" :alt="product.name" />
      <div class="product-overlay">
        <button class="btn btn-primary" @click.stop="addToCart">Add to Cart</button>
      </div>
    </div>
    <div class="product-info">
      <h3>{{ product.name }}</h3>
      <p class="product-category">{{ product.category }}</p>
      <p class="product-price">${{ product.price.toFixed(2) }}</p>
    </div>
  </div>
</template>

<script>
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
      goToProduct,
      addToCart
    }
  }
}
</script>

<style scoped>
.product-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.product-image {
  position: relative;
  width: 100%;
  padding-top: 100%; /* Square aspect ratio */
  overflow: hidden;
  background-color: var(--sandy-beige);
}

.product-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.product-card:hover .product-image img {
  transform: scale(1.05);
}

.product-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(61, 40, 23, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.product-card:hover .product-overlay {
  opacity: 1;
}

.product-overlay .btn {
  padding: 10px 20px;
  font-size: 14px;
}

.product-info {
  padding: 1rem;
}

.product-info h3 {
  font-size: 18px;
  margin-bottom: 0.5rem;
  color: var(--deep-brown);
}

.product-category {
  font-size: 14px;
  color: var(--terracotta);
  text-transform: capitalize;
  margin-bottom: 0.5rem;
}

.product-price {
  font-size: 20px;
  font-weight: 600;
  color: var(--turquoise);
  margin: 0;
}
</style>

