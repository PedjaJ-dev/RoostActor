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
const telefon = ref("");  // Dodato polje za telefon

const fetchKorisnik = async () => { 
  try { 
    const response = await axios.get(`/api/korisnik/${id}`); 
    ime.value = response.data.ime; 
    prezime.value = response.data.prezime; 
    email.value = response.data.email; 
    telefon.value = response.data.telefon;  // Učitavanje telefona
  } catch (error) { 
    if (error.response.status == 401) { 
      router.push("/login").then(() => toast.error(error.response.data.message)); 
    } else { 
      toast.error(error.response.data.message || error.message); 
    } 
  } 
}; 

const handleSubmit = async (event) => { 
  event.preventDefault(); 
  try { 
    const response = await axios.put(`/api/korisnik-izmena/${id}`, { 
      ime: ime.value, 
      prezime: prezime.value, 
      email: email.value, 
      telefon: telefon.value,  // Poslato polje za telefon
    }); 
    router.push("/korisnici").then(() => 
      toast.success(response.data.message)
    ); 
  } catch (error) { 
    toast.error(error.response.data.message || error.message); 
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
        <label for="telefon" class="form-label">Telefon</label>
        <input 
          type="text" 
          class="form-control" 
          id="telefon" 
          v-model="telefon" 
          required 
        />
      </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>
