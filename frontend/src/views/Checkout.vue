<template>
  <div class="checkout">
    <div class="container">
      <h1 class="page-title">Checkout</h1>
      
      <div v-if="cartItems.length === 0" class="empty-cart">
        <p>Your cart is empty.</p>
        <router-link to="/shop" class="btn btn-primary">Continue Shopping</router-link>
      </div>
      
      <div v-else class="checkout-content">
        <form @submit.prevent="submitOrder" class="checkout-form">
          <div class="form-section">
            <h2>Shipping Information</h2>
            
            <div class="form-group">
              <label for="name">Full Name *</label>
              <input 
                type="text" 
                id="name" 
                v-model="formData.customer_name" 
                required 
                placeholder="John Doe"
              />
            </div>
            
            <div class="form-group">
              <label for="email">Email Address *</label>
              <input 
                type="email" 
                id="email" 
                v-model="formData.customer_email" 
                required 
                placeholder="john@example.com"
              />
            </div>
            
            <div class="form-group">
              <label for="address">Shipping Address *</label>
              <textarea 
                id="address" 
                v-model="formData.address" 
                required 
                rows="4"
                placeholder="Street address, City, State, ZIP Code"
              ></textarea>
            </div>
          </div>
          
          <div class="form-section">
            <h2>Order Summary</h2>
            <div class="order-items">
              <div 
                class="order-item" 
                v-for="(item, index) in cartItems" 
                :key="index"
              >
                <div class="item-info">
                  <img :src="item.image_url || '/placeholder.jpg'" :alt="item.name" />
                  <div>
                    <h4>{{ item.name }}</h4>
                    <p v-if="item.size">Size: {{ item.size }}</p>
                    <p>Quantity: {{ item.quantity }}</p>
                  </div>
                </div>
                <p class="item-price">${{ (item.price * item.quantity).toFixed(2) }}</p>
              </div>
            </div>
            
            <div class="order-totals">
              <div class="total-row">
                <span>Subtotal:</span>
                <span>${{ subtotal.toFixed(2) }}</span>
              </div>
              <div class="total-row">
                <span>Shipping:</span>
                <span>${{ shipping.toFixed(2) }}</span>
              </div>
              <div class="total-row final">
                <span>Total:</span>
                <span>${{ total.toFixed(2) }}</span>
              </div>
            </div>
            
            <button 
              type="submit" 
              class="btn btn-primary btn-large"
              :disabled="submitting"
            >
              {{ submitting ? 'Processing...' : 'Place Order' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default {
  name: 'Checkout',
  setup() {
    const router = useRouter()
    const cartItems = ref([])
    const submitting = ref(false)
    const shipping = ref(10.00)
    
    const formData = ref({
      customer_name: '',
      customer_email: '',
      address: ''
    })
    
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
    
    const submitOrder = async () => {
      if (cartItems.value.length === 0) {
        alert('Your cart is empty!')
        return
      }
      
      submitting.value = true
      
      try {
        const orderData = {
          customer_name: formData.value.customer_name,
          customer_email: formData.value.customer_email,
          address: formData.value.address,
          total_price: total.value,
          items: cartItems.value.map(item => ({
            product_id: item.product_id,
            quantity: item.quantity
          }))
        }
        
        const response = await axios.post('/api/orders', orderData)
        
        if (response.data.success) {
          // Clear cart
          localStorage.removeItem('cart')
          window.dispatchEvent(new Event('cartUpdated'))
          
          // Redirect to success page or show confirmation
          alert(`Order placed successfully! Order ID: ${response.data.order_id}`)
          router.push('/')
        }
      } catch (error) {
        console.error('Error placing order:', error)
        alert('Failed to place order. Please try again.')
      } finally {
        submitting.value = false
      }
    }
    
    onMounted(() => {
      loadCart()
      if (cartItems.value.length === 0) {
        router.push('/cart')
      }
    })
    
    return {
      cartItems,
      formData,
      shipping,
      subtotal,
      total,
      submitting,
      submitOrder
    }
  }
}
</script>

<style scoped>
.checkout {
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

.checkout-content {
  max-width: 900px;
  margin: 0 auto;
}

.checkout-form {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 3rem;
}

.form-section {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-section h2 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: var(--deep-brown);
  border-bottom: 2px solid var(--sandy-beige);
  padding-bottom: 0.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--deep-brown);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px;
  border: 2px solid var(--sandy-beige);
  border-radius: 4px;
  font-size: 16px;
  font-family: var(--font-sans);
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--terracotta);
}

.order-items {
  margin-bottom: 2rem;
}

.order-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid var(--sandy-beige);
}

.order-item:last-child {
  border-bottom: none;
}

.item-info {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.item-info img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 4px;
  background-color: var(--sandy-beige);
}

.item-info h4 {
  font-size: 1rem;
  margin-bottom: 0.25rem;
}

.item-info p {
  font-size: 0.9rem;
  color: var(--terracotta);
  margin: 0.25rem 0;
}

.item-price {
  font-weight: 600;
  color: var(--turquoise);
  font-size: 1.1rem;
}

.order-totals {
  margin-bottom: 2rem;
  padding-top: 1rem;
  border-top: 2px solid var(--sandy-beige);
}

.total-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
}

.total-row.final {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--deep-brown);
  padding-top: 1rem;
  border-top: 2px solid var(--sandy-beige);
  margin-top: 1rem;
}

.btn-large {
  width: 100%;
  padding: 16px;
  font-size: 18px;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

@media (max-width: 968px) {
  .checkout-form {
    grid-template-columns: 1fr;
  }
}
</style>

