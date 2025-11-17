<script>
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import ProductCard from '../components/ProductCard.vue'

export default {
  name: 'Shop',
  components: {
    ProductCard
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const products = ref([])
    const categories = ref([])
    const loading = ref(true)
    const selectedCategories = ref([])
    const minPrice = ref(null)
    const maxPrice = ref(null)
    const materialFilter = ref('')
    const lastCategoryParam = ref(null)

    const filteredProducts = computed(() => {
      let filtered = [...products.value]

      if (selectedCategories.value.length > 0) {
        filtered = filtered.filter(p => selectedCategories.value.includes(p.category))
      }

      if (minPrice.value !== null && minPrice.value !== '') {
        filtered = filtered.filter(p => p.price >= minPrice.value)
      }

      if (maxPrice.value !== null && maxPrice.value !== '') {
        filtered = filtered.filter(p => p.price <= maxPrice.value)
      }

      if (materialFilter.value) {
        filtered = filtered.filter(
          p => p.material && p.material.toLowerCase().includes(materialFilter.value.toLowerCase())
        )
      }

      return filtered
    })

    const applyFilters = () => {
      // Computed handles filtering; this is kept for clarity / future hooks.
    }

    const clearCategoryQuery = () => {
      const newQuery = { ...route.query }
      delete newQuery.category
      router.replace({ query: newQuery })
      lastCategoryParam.value = null
    }

    const clearFilters = () => {
      selectedCategories.value = []
      minPrice.value = null
      maxPrice.value = null
      materialFilter.value = ''
      clearCategoryQuery()
    }

    const syncCategoryFromRoute = () => {
      const categoryParam = route.query.category
      if (categoryParam && categoryParam !== lastCategoryParam.value) {
        selectedCategories.value = [categoryParam]
        lastCategoryParam.value = categoryParam
      } else if (!categoryParam && lastCategoryParam.value) {
        selectedCategories.value = []
        lastCategoryParam.value = null
      }
    }

    watch(
      () => route.query.category,
      () => {
        syncCategoryFromRoute()
      }
    )

    onMounted(async () => {
      try {
        syncCategoryFromRoute()

        const [productsRes, categoriesRes] = await Promise.all([
          axios.get('/api/products'),
          axios.get('/api/categories')
        ])

        products.value = productsRes.data
        categories.value = categoriesRes.data
        loading.value = false
      } catch (error) {
        console.error('Error fetching data:', error)
        loading.value = false
      }
    })

    return {
      products,
      categories,
      loading,
      selectedCategories,
      minPrice,
      maxPrice,
      materialFilter,
      filteredProducts,
      applyFilters,
      clearFilters
    }
  }
}
</script>

<template>
  <div class="shop">
    <div class="container">
      <h1 class="page-title">Shop</h1>
      
      <div class="shop-content">
        <!-- Filters -->
        <aside class="filters">
          <h3>Filters</h3>
          
          <div class="filter-group">
            <h4>Category</h4>
            <label v-for="cat in categories" :key="cat">
              <input 
                type="checkbox" 
                :value="cat" 
                v-model="selectedCategories"
                @change="applyFilters"
              />
              {{ cat }}
            </label>
          </div>
          
          <div class="filter-group">
            <h4>Price Range</h4>
            <div class="price-inputs">
              <input 
                type="number" 
                v-model.number="minPrice" 
                placeholder="Min" 
                @input="applyFilters"
              />
              <span>to</span>
              <input 
                type="number" 
                v-model.number="maxPrice" 
                placeholder="Max" 
                @input="applyFilters"
              />
            </div>
          </div>
          
          <div class="filter-group">
            <h4>Material</h4>
            <input 
              type="text" 
              v-model="materialFilter" 
              placeholder="Search material..."
              @input="applyFilters"
            />
          </div>
          
          <button @click="clearFilters" class="btn btn-outline">Clear Filters</button>
        </aside>
        
        <!-- Products -->
        <main class="products-section">
          <div v-if="loading" class="loading">Loading products...</div>
          <div v-else-if="filteredProducts.length === 0" class="no-products">
            <p>No products found. Try adjusting your filters.</p>
          </div>
          <div v-else class="products-grid">
            <ProductCard 
              v-for="product in filteredProducts" 
              :key="product.id" 
              :product="product" 
            />
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<style scoped>
.shop {
  padding: 2rem 0;
  min-height: 60vh;
}

.page-title {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 3rem;
  color: var(--deep-brown);
}

.shop-content {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 2rem;
}

.filters {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  height: fit-content;
  position: sticky;
  top: 100px;
}

.filters h3 {
  margin-bottom: 1.5rem;
  color: var(--deep-brown);
}

.filter-group {
  margin-bottom: 1.5rem;
}

.filter-group h4 {
  font-size: 1rem;
  margin-bottom: 0.75rem;
  color: var(--terracotta);
}

.filter-group label {
  display: block;
  margin-bottom: 0.5rem;
  cursor: pointer;
  text-transform: capitalize;
}

.filter-group input[type="checkbox"] {
  margin-right: 0.5rem;
}

.price-inputs {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.price-inputs input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.filter-group input[type="text"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.products-section {
  min-height: 400px;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 2.5rem;
  padding: 1rem 0;
}

.loading,
.no-products {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--terracotta);
  font-size: 1.2rem;
}

@media (max-width: 968px) {
  .shop-content {
    grid-template-columns: 1fr;
  }
  
  .filters {
    position: static;
  }
}
</style>

