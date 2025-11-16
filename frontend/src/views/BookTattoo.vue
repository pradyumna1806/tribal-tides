<template>
  <div class="book-tattoo">
    <div class="container">
      <h1 class="page-title">Book a Temporary Tattoo</h1>
      <p class="page-subtitle">Experience our unique temporary tattoo designs inspired by coastal and tribal art</p>
      
      <div class="booking-content">
        <div class="booking-info">
          <h2>About Our Temporary Tattoos</h2>
          <p>
            Our temporary tattoos are handcrafted with high-quality, safe materials that last 3-7 days. 
            Perfect for festivals, events, or just expressing your style. Each design is inspired by 
            coastal and tribal aesthetics.
          </p>
          
          <div class="info-cards">
            <div class="info-card">
              <h3>🎨 Custom Designs</h3>
              <p>Choose from our collection or request a custom design</p>
            </div>
            <div class="info-card">
              <h3>⏱️ Quick Application</h3>
              <p>Professional application takes just 15-30 minutes</p>
            </div>
            <div class="info-card">
              <h3>✨ Safe & Non-Permanent</h3>
              <p>Made with skin-safe, hypoallergenic materials</p>
            </div>
          </div>
        </div>
        
        <form @submit.prevent="submitBooking" class="booking-form">
          <h2>Booking Form</h2>
          
          <div class="form-group">
            <label for="name">Full Name *</label>
            <input 
              type="text" 
              id="name" 
              v-model="formData.name" 
              required 
              placeholder="Your full name"
            />
          </div>
          
          <div class="form-group">
            <label for="date">Preferred Date *</label>
            <input 
              type="date" 
              id="date" 
              v-model="formData.date" 
              required 
              :min="minDate"
            />
          </div>
          
          <div class="form-group">
            <label for="time">Preferred Time *</label>
            <input 
              type="time" 
              id="time" 
              v-model="formData.time" 
              required 
            />
          </div>
          
          <div class="form-group">
            <label for="style">Tattoo Style/Design *</label>
            <select 
              id="style" 
              v-model="formData.style" 
              required
            >
              <option value="">Select a style</option>
              <option value="Coastal Waves">Coastal Waves</option>
              <option value="Tribal Geometric">Tribal Geometric</option>
              <option value="Seashell Pattern">Seashell Pattern</option>
              <option value="Ocean Mandala">Ocean Mandala</option>
              <option value="Custom Design">Custom Design</option>
            </select>
          </div>
          
          <div class="form-group">
            <label for="notes">Additional Notes (Optional)</label>
            <textarea 
              id="notes" 
              v-model="formData.notes" 
              rows="4"
              placeholder="Any specific requests or details about your desired design..."
            ></textarea>
          </div>
          
          <button 
            type="submit" 
            class="btn btn-primary btn-large"
            :disabled="submitting"
          >
            {{ submitting ? 'Submitting...' : 'Book Appointment' }}
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
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'BookTattoo',
  setup() {
    const submitting = ref(false)
    const successMessage = ref('')
    const errorMessage = ref('')
    
    const formData = ref({
      name: '',
      date: '',
      time: '',
      style: '',
      notes: ''
    })
    
    const minDate = computed(() => {
      const today = new Date()
      today.setDate(today.getDate() + 1) // Minimum date is tomorrow
      return today.toISOString().split('T')[0]
    })
    
    const submitBooking = async () => {
      submitting.value = true
      successMessage.value = ''
      errorMessage.value = ''
      
      try {
        const bookingData = {
          name: formData.value.name,
          date: formData.value.date,
          time: formData.value.time,
          style: formData.value.style + (formData.value.notes ? ` - ${formData.value.notes}` : '')
        }
        
        const response = await axios.post('/api/book-tattoo', bookingData)
        
        if (response.data.success) {
          successMessage.value = `Booking confirmed! Your booking ID is ${response.data.booking_id}. We'll contact you soon to confirm your appointment.`
          
          // Reset form
          formData.value = {
            name: '',
            date: '',
            time: '',
            style: '',
            notes: ''
          }
        }
      } catch (error) {
        console.error('Error booking tattoo:', error)
        errorMessage.value = 'Failed to submit booking. Please try again or contact us directly.'
      } finally {
        submitting.value = false
      }
    }
    
    return {
      formData,
      minDate,
      submitting,
      successMessage,
      errorMessage,
      submitBooking
    }
  }
}
</script>

<style scoped>
.book-tattoo {
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

.booking-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.booking-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.booking-info > p {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 2rem;
  color: var(--deep-brown);
}

.info-cards {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-left: 4px solid var(--turquoise);
}

.info-card h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  color: var(--deep-brown);
}

.info-card p {
  color: var(--terracotta);
  margin: 0;
}

.booking-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.booking-form h2 {
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
  .booking-content {
    grid-template-columns: 1fr;
  }
  
  .page-title {
    font-size: 2rem;
  }
}
</style>

