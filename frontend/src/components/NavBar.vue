<template>
  <nav class="navbar">
    <div class="container">
      <div class="nav-content">
        <router-link to="/" class="logo">
          <h1>Tribal Tides</h1>
        </router-link>
        
        <ul class="nav-links">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/shop">Shop</router-link></li>
          <li><router-link to="/book-tattoo">Book Tattoo</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/contact">Contact</router-link></li>
        </ul>
        
        <div class="nav-actions">
          <router-link to="/cart" class="cart-icon">
            <span class="cart-badge" v-if="cartCount > 0">{{ cartCount }}</span>
            🛒
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'NavBar',
  setup() {
    const cartCount = ref(0)
    
    const updateCartCount = () => {
      const cart = JSON.parse(localStorage.getItem('cart') || '[]')
      cartCount.value = cart.reduce((sum, item) => sum + item.quantity, 0)
    }
    
    onMounted(() => {
      updateCartCount()
      window.addEventListener('cartUpdated', updateCartCount)
    })
    
    onUnmounted(() => {
      window.removeEventListener('cartUpdated', updateCartCount)
    })
    
    return {
      cartCount
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 1rem 0;
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  font-size: 28px;
  color: var(--terracotta);
  margin: 0;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.nav-links a {
  font-weight: 500;
  color: var(--deep-brown);
  position: relative;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  color: var(--terracotta);
}

.nav-links a.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--terracotta);
}

.cart-icon {
  font-size: 24px;
  position: relative;
  display: inline-block;
}

.cart-badge {
  position: absolute;
  top: -8px;
  right: -8px;
  background-color: var(--turquoise);
  color: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 600;
}

@media (max-width: 768px) {
  .nav-links {
    gap: 1rem;
    font-size: 14px;
  }
  
  .logo h1 {
    font-size: 22px;
  }
}
</style>

