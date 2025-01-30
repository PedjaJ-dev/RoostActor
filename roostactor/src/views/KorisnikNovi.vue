<script setup>
import { ref } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import { useRouter } from "vue-router";
import FormContainer from "@/components/FormContainer.vue";

const router = useRouter();

const ime = ref("");
const prezime = ref("");
const uloga = ref("administrator");  // Set default value
const email = ref("");
const telefon = ref("");  // Dodajte ovo
const lozinka = ref("");

const handleSubmit = async (event) => {
  event.preventDefault();
  try {
    const response = await axios.post("http://localhost:5000/korisnici", {
      email: email.value, 
      ime: ime.value,
      prezime: prezime.value,
      telefon: telefon.value, 
      uloga: uloga.value,
      lozinka: lozinka.value
    });
    // Success redirect with success message
    router.push("/korisnici").then(() => toast.success(response.data.message || "Korisnik uspešno dodat."));
  } catch (error) {
    // If no specific error message, show default error
    const errorMessage = error.response?.data?.message || error.message || "Greška prilikom dodavanja korisnika.";
    toast.error(errorMessage);
  }
};
</script>

<template>
  <FormContainer title="Novi korisnik">
    <form @submit="handleSubmit">
      <div class="mb-3">
        <label for="ime" class="form-label">Ime</label>
        <input 
          type="text" 
          class="form-control"
          id="ime" 
          v-model="ime" 
          required 
          autocomplete="given-name"
          size="50"
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
          autocomplete="family-name"
        />
      </div>

      <div class="mb-3">
        <label for="uloga" class="form-label">Uloga</label>
        <select id="uloga" class="form-select" v-model="uloga" required>
          <option disabled value="">Izaberi ulogu</option>
          <option value="Administrator">Administrator</option>
          <option value="Korisnik">Korisnik</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input 
          type="email" 
          class="form-control" 
          id="email" 
          v-model="email" 
          required 
          autocomplete="email"
        />
      </div>

      <div class="mb-3">
        <label for="telefon" class="form-label">Telefon</label>
        <input 
          type="tel" 
          class="form-control" 
          id="telefon" 
          v-model="telefon" 
          required 
          autocomplete="tel"
        />
      </div>

      <div class="mb-3">
        <label for="lozinka" class="form-label">Lozinka</label>
        <input 
          type="password" 
          class="form-control" 
          id="lozinka" 
          v-model="lozinka" 
          required 
          autocomplete="new-password"
        />
      </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>

<style scoped>
</style>




