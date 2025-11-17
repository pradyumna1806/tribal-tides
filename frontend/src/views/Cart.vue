<template>
  <div class="cart">
    <div class="container">
      <h1 class="page-title">Shopping Cart</h1>
      
      <div v-if="cartItems.length === 0" class="empty-cart">
        <p>Your cart is empty.</p>
        <router-link to="/shop" class="btn btn-primary">Continue Shopping</router-link>
      </div>
      
      <div v-else class="cart-content">
        <div class="cart-items">
          <div class="cart-item" v-for="(item, index) in cartItems" :key="index">
            <div class="item-image">
              <img :src="item.image_url || '/placeholder.jpg'" :alt="item.name" />
            </div>
            <div class="item-info">
              <h3>{{ item.name }}</h3>
              <p v-if="item.size">Size: {{ item.size }}</p>
              <p class="item-price">₹{{ formatPrice(item.price) }}</p>
            </div>
            <div class="item-quantity">
              <button @click="updateQuantity(index, item.quantity - 1)">-</button>
              <span>{{ item.quantity }}</span>
              <button @click="updateQuantity(index, item.quantity + 1)">+</button>
            </div>
            <div class="item-total">
              <p>₹{{ formatPrice(item.price * item.quantity) }}</p>
            </div>
            <button @click="removeItem(index)" class="remove-btn">×</button>
          </div>
        </div>
        
        <div class="cart-summary">
          <h3>Order Summary</h3>
          <div class="summary-row">
            <span>Subtotal:</span>
            <span>₹{{ formatPrice(subtotal) }}</span>
          </div>
          <div class="summary-row">
            <span>Shipping:</span>
            <span>₹{{ formatPrice(shipping) }}</span>
          </div>
          <div class="summary-row total">
            <span>Total:</span>
            <span>₹{{ formatPrice(total) }}</span>
          </div>
          <router-link to="/checkout" class="btn btn-primary btn-large">
            Proceed to Checkout
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'Cart',
  setup() {
    const cartItems = ref([])
    const shipping = ref(100.00) // Shipping in INR

    const formatPrice = (price) => {
      return new Intl.NumberFormat('en-IN').format(price.toFixed(0))
    }

    const subtotal = computed(() => {
      return cartItems.value.reduce((sum, item) => sum + (item.price * item.quantity), 0)
    })

    const total = computed(() => {
      return subtotal.value + shipping.value
    })

    const loadCart = () => {
      const cart = localStorage.getItem('cart')
      cartItems.value = cart ? JSON.parse(cart) : []
    }

    const updateQuantity = (index, newQuantity) => {
      if (newQuantity < 1) {
        removeItem(index)
        return
      }
      cartItems.value[index].quantity = newQuantity
      saveCart()
    }

    const removeItem = (index) => {
      cartItems.value.splice(index, 1)
      saveCart()
    }

    const saveCart = () => {
      localStorage.setItem('cart', JSON.stringify(cartItems.value))
      window.dispatchEvent(new Event('cartUpdated'))
    }

    onMounted(() => {
      loadCart()
      // Listen for cart updates
      window.addEventListener('cartUpdated', loadCart)
    })

    return {
      cartItems,
      shipping,
      subtotal,
      total,
      formatPrice,
      updateQuantity,
      removeItem
    }
  }
}
</script>

<style scoped>
.cart {
  padding: 2rem 0;
  min-height: 60vh;
}

.page-title {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 3rem;
  color: var(--deep-brown);
}

.empty-cart {
  text-align: center;
  padding: 4rem 2rem;
}

.empty-cart p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: var(--terracotta);
}

.cart-content {
  display: grid;
  grid-template-columns: 1fr 350px;
  gap: 2rem;
}

.cart-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.cart-item {
  display: grid;
  grid-template-columns: 120px 1fr 150px 100px 40px;
  gap: 1rem;
  align-items: center;
  background: white;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.item-image {
  width: 120px;
  height: 120px;
  overflow: hidden;
  border-radius: 4px;
  background-color: var(--sandy-beige);
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-info h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.item-price {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--turquoise);
  margin-top: 0.5rem;
}

.item-quantity {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  justify-content: center;
}

.item-quantity button {
  width: 35px;
  height: 35px;
  border: 2px solid var(--deep-brown);
  background: white;
  border-radius: 4px;
  font-size: 18px;
}

.item-quantity button:hover {
  background: var(--sandy-beige);
}

.item-quantity span {
  font-size: 18px;
  font-weight: 600;
  min-width: 30px;
  text-align: center;
}

.item-total {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--deep-brown);
  text-align: right;
}

.remove-btn {
  background: transparent;
  color: var(--terracotta);
  font-size: 28px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.remove-btn:hover {
  background: var(--sandy-beige);
}

.cart-summary {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  height: fit-content;
  position: sticky;
  top: 100px;
}

.cart-summary h3 {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.summary-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.summary-row.total {
  font-size: 1.3rem;
  font-weight: 600;
  padding-top: 1rem;
  border-top: 2px solid var(--sandy-beige);
  margin-top: 1rem;
}

.btn-large {
  width: 100%;
  margin-top: 1.5rem;
  padding: 16px;
  font-size: 18px;
}

@media (max-width: 968px) {
  .cart-content {
    grid-template-columns: 1fr;
  }
  
  .cart-item {
    grid-template-columns: 100px 1fr;
    grid-template-rows: auto auto auto;
  }
  
  .item-quantity,
  .item-total,
  .remove-btn {
    grid-column: 2;
  }
  
  .cart-summary {
    position: static;
  }
}
</style>

