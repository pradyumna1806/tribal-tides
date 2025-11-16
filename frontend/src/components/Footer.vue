<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>Tribal Tides</h3>
          <p>Coastal & Tribal Fashion</p>
          <p>Bringing the spirit of the coast and tribal heritage to your wardrobe.</p>
        </div>
        
        <div class="footer-section">
          <h4>Quick Links</h4>
          <ul>
            <li><router-link to="/shop">Shop</router-link></li>
            <li><router-link to="/book-tattoo">Book Tattoo</router-link></li>
            <li><router-link to="/about">About Us</router-link></li>
            <li><router-link to="/contact">Contact</router-link></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Categories</h4>
          <ul>
            <li><router-link to="/shop?category=clothing">Clothing</router-link></li>
            <li><router-link to="/shop?category=accessories">Accessories</router-link></li>
            <li><router-link to="/shop?category=footwear">Footwear</router-link></li>
            <li><router-link to="/shop?category=jewelry">Jewelry</router-link></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Newsletter</h4>
          <p>Subscribe for updates and special offers</p>
          <form @submit.prevent="subscribeNewsletter" class="newsletter-form">
            <input type="email" v-model="email" placeholder="Your email" required>
            <button type="submit" class="btn btn-primary">Subscribe</button>
          </form>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2024 Tribal Tides. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Footer',
  setup() {
    const email = ref('')
    
    const subscribeNewsletter = () => {
      alert(`Thank you for subscribing with ${email.value}!`)
      email.value = ''
    }
    
    return {
      email,
      subscribeNewsletter
    }
  }
}
</script>

<style scoped>
.footer {
  background-color: var(--deep-brown);
  color: var(--sandy-beige);
  padding: 3rem 0 1rem;
  margin-top: 4rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section h3,
.footer-section h4 {
  color: var(--sandy-beige);
  margin-bottom: 1rem;
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 0.5rem;
}

.footer-section a {
  color: var(--sandy-beige);
  opacity: 0.8;
}

.footer-section a:hover {
  opacity: 1;
  color: var(--turquoise);
}

.newsletter-form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.newsletter-form input {
  padding: 10px;
  border: 1px solid var(--sandy-beige);
  border-radius: 4px;
  background-color: transparent;
  color: var(--sandy-beige);
}

.newsletter-form input::placeholder {
  color: var(--sandy-beige);
  opacity: 0.6;
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(245, 230, 211, 0.2);
  opacity: 0.8;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
  }
}
</style>

