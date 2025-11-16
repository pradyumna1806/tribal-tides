<template>
  <div class="contact">
    <div class="container">
      <h1 class="page-title">Contact Us</h1>
      <p class="page-subtitle">We'd love to hear from you! Get in touch with any questions or feedback.</p>
      
      <div class="contact-content">
        <div class="contact-info">
          <h2>Get in Touch</h2>
          <p>
            Have a question about our products? Want to customize an order? Or just want to say hello? 
            We're here to help!
          </p>
          
          <div class="info-cards">
            <div class="info-card">
              <div class="info-icon">📧</div>
              <h3>Email</h3>
              <p>hello@tribaltides.com</p>
              <p>support@tribaltides.com</p>
            </div>
            
            <div class="info-card">
              <div class="info-icon">📞</div>
              <h3>Phone</h3>
              <p>+1 (555) 123-4567</p>
              <p>Mon-Fri: 9am - 6pm EST</p>
            </div>
            
            <div class="info-card">
              <div class="info-icon">📍</div>
              <h3>Location</h3>
              <p>123 Coastal Avenue</p>
              <p>Beach City, BC 12345</p>
            </div>
            
            <div class="info-card">
              <div class="info-icon">💬</div>
              <h3>Social Media</h3>
              <p>@tribaltides</p>
              <p>Follow us for updates!</p>
            </div>
          </div>
        </div>
        
        <form @submit.prevent="submitContact" class="contact-form">
          <h2>Send us a Message</h2>
          
          <div class="form-group">
            <label for="name">Name *</label>
            <input 
              type="text" 
              id="name" 
              v-model="formData.name" 
              required 
              placeholder="Your name"
            />
          </div>
          
          <div class="form-group">
            <label for="email">Email *</label>
            <input 
              type="email" 
              id="email" 
              v-model="formData.email" 
              required 
              placeholder="your.email@example.com"
            />
          </div>
          
          <div class="form-group">
            <label for="subject">Subject *</label>
            <select 
              id="subject" 
              v-model="formData.subject" 
              required
            >
              <option value="">Select a subject</option>
              <option value="General Inquiry">General Inquiry</option>
              <option value="Product Question">Product Question</option>
              <option value="Order Support">Order Support</option>
              <option value="Tattoo Booking">Tattoo Booking</option>
              <option value="Custom Order">Custom Order</option>
              <option value="Feedback">Feedback</option>
            </select>
          </div>
          
          <div class="form-group">
            <label for="message">Message *</label>
            <textarea 
              id="message" 
              v-model="formData.message" 
              required 
              rows="6"
              placeholder="Tell us how we can help..."
            ></textarea>
          </div>
          
          <button 
            type="submit" 
            class="btn btn-primary btn-large"
            :disabled="submitting"
          >
            {{ submitting ? 'Sending...' : 'Send Message' }}
          </button>
          
          <div v-if="successMessage" class="success-message">
            {{ successMessage }}
          </div>
          
          <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Contact',
  setup() {
    const submitting = ref(false)
    const successMessage = ref('')
    const errorMessage = ref('')
    
    const formData = ref({
      name: '',
      email: '',
      subject: '',
      message: ''
    })
    
    const submitContact = async () => {
      submitting.value = true
      successMessage.value = ''
      errorMessage.value = ''
      
      // Simulate form submission (in a real app, this would call an API)
      setTimeout(() => {
        successMessage.value = 'Thank you for your message! We\'ll get back to you within 24 hours.'
        
        // Reset form
        formData.value = {
          name: '',
          email: '',
          subject: '',
          message: ''
        }
        
        submitting.value = false
      }, 1000)
    }
    
    return {
      formData,
      submitting,
      successMessage,
      errorMessage,
      submitContact
    }
  }
}
</script>

<style scoped>
.contact {
  padding: 2rem 0;
  min-height: 60vh;
}

.page-title {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.page-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: var(--terracotta);
  margin-bottom: 3rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.contact-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.contact-info > p {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 2rem;
  color: var(--deep-brown);
}

.info-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  border-top: 4px solid var(--turquoise);
}

.info-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.info-card h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: var(--deep-brown);
}

.info-card p {
  font-size: 0.95rem;
  color: var(--terracotta);
  margin: 0.25rem 0;
}

.contact-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.contact-form h2 {
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
.form-group select,
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
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--terracotta);
}

.btn-large {
  width: 100%;
  padding: 16px;
  font-size: 18px;
  margin-top: 1rem;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.success-message {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #d4edda;
  color: #155724;
  border-radius: 4px;
  border: 1px solid #c3e6cb;
}

.error-message {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f8d7da;
  color: #721c24;
  border-radius: 4px;
  border: 1px solid #f5c6cb;
}

@media (max-width: 968px) {
  .contact-content {
    grid-template-columns: 1fr;
  }
  
  .info-cards {
    grid-template-columns: 1fr;
  }
  
  .page-title {
    font-size: 2rem;
  }
}
</style>

