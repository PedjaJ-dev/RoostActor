<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import { useRouter, useRoute } from "vue-router";
import FormContainer from "@/components/FormContainer.vue";

const router = useRouter();
const route = useRoute();
const id = route.params.id; // Getting the project ID from the URL

const naziv = ref("");
const tim = ref("");
const opis = ref("");

// Fetch project data
onMounted(() => {
  fetchProject();
});

// Function to fetch the project data based on the provided ID
const fetchProject = async () => {
  try {
    const response = await axios.get(`http://localhost:5000/projekti/${id}`);
    console.log(response.data);  // Log the response to check the value of 'status'

    naziv.value = response.data.naziv;
    tim.value = response.data.tim;
    opis.value = response.data.opis;

  } catch (error) {
    toast.error(error.response?.data?.message || "Greška pri učitavanju podataka.");
  }
};
</script>

<template>
  <FormContainer title="Detalji Projekta">
    <br>
    <div class="mb-3">
      <label for="naziv" class="form-label">Naziv Projekta</label>
      <input
        type="text"
        class="form-control"
        id="naziv"
        v-model="naziv"
        readonly
      />
    </div>

    <div class="mb-3">
      <label for="tim" class="form-label">Tim</label>
      <input
        type="text"
        class="form-control large-input"
        id="tim"
        v-model="tim"
        readonly
      />
    </div>

    <div class="mb-3">
      <label for="opis" class="form-label">Opis</label>
      <input
        type="text"
        class="form-control large-input"
        id="opis"
        v-model="opis"
        readonly
      />
    </div>
  </FormContainer>
</template>

<style scoped>
.form-label {
  font-size: 1.25rem; /* Larger font size for labels */
  font-weight: bold;
  margin-bottom: 0.5rem;
}

/* Larger input fields for tim and opis */
.large-input {
  font-size: 1.1rem; /* Increase font size for the inputs */
  padding: 0.75rem;  /* Increase padding for a bigger input field */
  height:200px;     /* Increase height of the input field */
}
</style>


