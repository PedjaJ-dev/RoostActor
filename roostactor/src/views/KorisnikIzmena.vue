<script setup>
import { ref, onMounted } from "vue"; 
import axios from "axios"; 
import { useRoute } from "vue-router"; 
import { useRouter } from "vue-router"; 
import FormContainer from "@/components/FormContainer.vue"; 
import { toast } from "vue3-toastify"; 

const router = useRouter(); 
const route = useRoute(); 
const id = route.params.id; 

const ime = ref(""); 
const prezime = ref(""); 
const email = ref(""); 
const uloga = ref(""); 

// Retrieve token from local storage or other storage mechanism
const token = localStorage.getItem('authToken'); 

// Function to fetch user data
const fetchKorisnik = async () => { 
  try { 
    const response = await axios.get(`http://localhost:5000/korisnici/${id}`, {
      headers: {
        Authorization: `Bearer ${token}` // Add the Authorization header
      }
    }); 
    ime.value = response.data.ime; 
    prezime.value = response.data.prezime; 
    email.value = response.data.email; 
    uloga.value = response.data.uloga; 
  } catch (error) { 
    if (error.response && error.response.status === 401) { 
      router.push("/login").then(() => toast.error(error.response.data.message)); 
    } else { 
      toast.error(error.response.data?.message || error.message); 
    } 
  } 
}; 

// Handle form submission
const handleSubmit = async (event) => { 
  event.preventDefault(); 
  try { 
    const response = await axios.put(`http://localhost:5000/korisnik-izmena/${id}`, {
      ime: ime.value,
      prezime: prezime.value,
      email: email.value,
      uloga: uloga.value,
    }, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}` // Add the Authorization header
      }
    });
    router.push("/korisnici").then(() => 
      toast.success(response.data.message)); 
  } catch (error) { 
    toast.error(error.response?.data?.message || error.message); 
  } 
}; 

onMounted(() => { 
  fetchKorisnik(); 
}); 
</script>

<template>
  <FormContainer title="Izmena korisnika">
    <form @submit="handleSubmit">
      <div class="mb-3">
        <label for="ime" class="form-label">Ime</label>
        <input 
          type="text" 
          class="form-control" 
          id="ime" 
          v-model="ime" 
          required 
        />
      </div>

      <div class="mb-3">
        <label for="prezime" class="form-label">Prezime</label>
        <input 
          type="text" 
          class="form-control" 
          id="prezime" 
          v-model="prezime" 
          required 
        />
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input 
          type="email" 
          class="form-control" 
          id="email" 
          v-model="email" 
          required 
        />
      </div>

      <div class="mb-3">
        <label for="uloga" class="form-label">Uloga</label>
        <select id="uloga" class="form-select" v-model="uloga" required>
          <option value="" disabled>Select role</option>
          <option value="Administrator">Administrator</option>
          <option value="Korisnik">Korisnik</option>
        </select>
      </div>



      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>


