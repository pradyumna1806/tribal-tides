<template>
  <div class="about">
    <div class="container">
      <div class="about-hero">
        <h1 class="page-title">About Tribal Tides</h1>
        <p class="hero-subtitle">Where Coastal Vibes Meet Tribal Heritage</p>
      </div>
      
      <section class="about-section">
        <div class="section-content">
          <div class="text-content">
            <h2>Our Story</h2>
            <p>
              Tribal Tides was born from a passion for blending the free-spirited essence of coastal 
              living with the rich, meaningful patterns of tribal art. We believe that fashion should 
              tell a story, connect us to nature, and celebrate cultural heritage.
            </p>
            <p>
              Founded in 2024, our brand has been dedicated to creating unique, high-quality pieces 
              that resonate with those who seek authenticity and style. Each item in our collection 
              is carefully curated to bring together the best of both worlds.
            </p>
          </div>
          <div class="image-placeholder">
            <div class="placeholder-content">
              <span>🌊</span>
              <p>Coastal & Tribal</p>
            </div>
          </div>
        </div>
      </section>
      
      <section class="about-section values">
        <h2 class="section-title">Our Values</h2>
        <div class="values-grid">
          <div class="value-card">
            <div class="value-icon">🌿</div>
            <h3>Sustainability</h3>
            <p>We're committed to using eco-friendly materials and ethical production practices.</p>
          </div>
          <div class="value-card">
            <div class="value-icon">✨</div>
            <h3>Quality</h3>
            <p>Every piece is crafted with attention to detail and built to last.</p>
          </div>
          <div class="value-card">
            <div class="value-icon">🎨</div>
            <h3>Authenticity</h3>
            <p>Our designs are inspired by real cultural traditions and natural beauty.</p>
          </div>
          <div class="value-card">
            <div class="value-icon">❤️</div>
            <h3>Community</h3>
            <p>We support local artisans and give back to the communities that inspire us.</p>
          </div>
        </div>
      </section>
      
      <section class="about-section">
        <h2 class="section-title">What We Offer</h2>
        <div class="offerings-grid">
          <div class="offering-item">
            <h3>Clothing</h3>
            <p>From flowing maxi dresses to comfortable tunics, our clothing collection embodies coastal comfort with tribal flair.</p>
          </div>
          <div class="offering-item">
            <h3>Accessories</h3>
            <p>Complete your look with our handpicked accessories including scarves, bags, and statement pieces.</p>
          </div>
          <div class="offering-item">
            <h3>Footwear</h3>
            <p>Step into style with our collection of beach sandals and tribal-inspired moccasins.</p>
          </div>
          <div class="offering-item">
            <h3>Jewelry</h3>
            <p>Adorn yourself with our unique jewelry pieces featuring turquoise, seashells, and tribal patterns.</p>
          </div>
          <div class="offering-item">
            <h3>Temporary Tattoos</h3>
            <p>Express yourself with our custom temporary tattoo designs, perfect for festivals and special events.</p>
          </div>
        </div>
      </section>
      
      <section class="about-section cta">
        <h2>Join the Tribe</h2>
        <p>Be part of our community and stay updated with new arrivals, special offers, and style inspiration.</p>
        <router-link to="/shop" class="btn btn-primary">Shop Now</router-link>
        <router-link to="/contact" class="btn btn-outline">Get in Touch</router-link>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style scoped>
.about {
  padding: 2rem 0;
  min-height: 60vh;
}

.about-hero {
  text-align: center;
  padding: 3rem 0;
  margin-bottom: 3rem;
}

.page-title {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.hero-subtitle {
  font-size: 1.5rem;
  color: var(--terracotta);
}

.about-section {
  margin-bottom: 4rem;
}

.section-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.text-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: var(--deep-brown);
}

.text-content p {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  color: var(--deep-brown);
}

.image-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: linear-gradient(135deg, var(--sandy-beige) 0%, var(--turquoise) 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.placeholder-content {
  text-align: center;
  color: var(--deep-brown);
}

.placeholder-content span {
  font-size: 4rem;
  display: block;
  margin-bottom: 1rem;
}

.placeholder-content p {
  font-size: 1.5rem;
  font-weight: 600;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: var(--deep-brown);
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.value-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.value-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.value-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.value-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.value-card p {
  color: var(--terracotta);
  line-height: 1.6;
}

.offerings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.offering-item {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-left: 4px solid var(--turquoise);
}

.offering-item h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.offering-item p {
  color: var(--terracotta);
  line-height: 1.6;
}

.cta {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, var(--sandy-beige) 0%, var(--turquoise) 100%);
  border-radius: 8px;
  margin-top: 4rem;
}

.cta h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--deep-brown);
}

.cta p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: var(--deep-brown);
}

.cta .btn {
  margin: 0 0.5rem;
}

@media (max-width: 768px) {
  .page-title {
    font-size: 2.5rem;
  }
  
  .section-content {
    grid-template-columns: 1fr;
  }
  
  .cta .btn {
    display: block;
    margin: 0.5rem auto;
    max-width: 200px;
  }
}
</style>

