<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import { useRouter, useRoute } from "vue-router";
import FormContainer from "@/components/FormContainer.vue";

const router = useRouter();
const route = useRoute();
const id = route.params.id; // Getting the project ID from the URL

// Declare the variables for the form inputs
const gledanost = ref("");
const prihodi = ref("");  // Optional, can be dynamically set based on form input
const ocena = ref("");

// Fetch the project data when the component is mounted
onMounted(() => {
  if (id) {
    fetchProject();
  } else {
    toast.error("ID nije pronađen u URL-u.");
  }
});

// Fetch project details based on the provided ID
const fetchProject = async () => {
  try {
    const response = await axios.get(`http://localhost:5000/statistika/${id}`);
    console.log(response);  // Prikazivanje celog odgovora
    gledanost.value = response.data.gledanost;
    prihodi.value = response.data.prihodi;
    ocena.value = response.data.ocena;
  } catch (error) {
    toast.error(error.response?.data?.message || "Greška pri učitavanju podataka.");
  }
};

// Handle form submission to update project
const handleSubmit = async (event) => {
  event.preventDefault();

  try {
    const response = await axios.put(`http://localhost:5000/statistika-izmena/${id}`, {
      gledanost: gledanost.value,
      prihodi: prihodi.value || "0", // Default to 0 if not provided
      ocena: ocena.value,
    });

    if (response && response.data) {
      router.push("/projekti").then(() => {
        toast.success(response.data.message || "Projekat uspešno izmenjen.");
      });
    } else {
      toast.error("Nevalidan odgovor sa servera.");
    }
  } catch (error) {
    toast.error(error.response?.data?.message || error.message);
  }
};
</script>

<template>
  <FormContainer title="Izmeni Statistiku">
    <form @submit="handleSubmit">

      <div class="mb-3">
        <label for="gledanost" class="form-label">Gledanost</label>
        <input
          type="text"
          class="form-control"
          id="gledanost"
          v-model="gledanost"
          required
        />
      </div>

      <div class="mb-3">
        <label for="prihodi" class="form-label">Prihodi</label>
        <input
          type="text"
          class="form-control large-input"
          id="prihodi"
          v-model="prihodi"
        />
      </div>

      <div class="mb-3">
        <label for="ocena" class="form-label">Ocena</label>
        <input
          type="text"
          class="form-control large-input"
          id="ocena"
          v-model="ocena"
          required
        />
      </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>

<style scoped>
</style>


