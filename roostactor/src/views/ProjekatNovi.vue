<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import { useRouter } from "vue-router";
import FormContainer from "@/components/FormContainer.vue";

const router = useRouter();

const naziv = ref("");
const tip = ref("");
const status = ref("");  // This can be dynamically set based on form input
const poceo = ref("");
const zavrsio = ref("");
const progres = ref("");

// Set the current date for the "poceo" field
onMounted(() => {
  const today = new Date();
  const formattedDate = today.toISOString().split("T")[0]; // Format: YYYY-MM-DD
  poceo.value = formattedDate;
});

const handleSubmit = async (event) => {
  event.preventDefault();
  
  try {
    const response = await axios.post("http://localhost:5000/projekti", {
      naziv: naziv.value,
      tip: tip.value,
      status: status.value || "U toku", // Dynamically use the selected status
      poceo: poceo.value,
      zavrsio: zavrsio.value,
      progres: progres.value || 0, // Default to 0 if no value is set
    });

    if (response && response.data) {
      router.push("/projekti").then(() => {
        toast.success(response.data.message || "Projekat uspešno dodat.");
      });
    } else {
      toast.error("Nevalidan odgovor sa servera.");
    }
  } catch (error) {
    if (error.response && error.response.data) {
      toast.error(error.response.data.message || error.message);
    } else {
      toast.error("Došlo je do greške pri slanju zahteva.");
    }
  }
};
</script>

<template>
  <FormContainer title="Novi Projekat">
    <form @submit="handleSubmit">
      <div class="mb-3">
        <label for="naziv" class="form-label">Naziv</label>
        <input
          type="text"
          class="form-control"
          id="naziv"
          v-model="naziv"
          required
          autocomplete="organization"
          size="50"
        />
      </div>

      <div class="mb-3">
        <label for="tip" class="form-label">Tip</label>
        <input
          type="text"
          class="form-control"
          id="tip"
          v-model="tip"
          required
        />
      </div>

      <div class="mb-3">
        <label for="status" class="form-label">Status</label>
        <select id="status" class="form-select" v-model="status" required>
          <option disabled value="">Izaberi status</option>
          <option value="U toku">U toku</option>
          <option value="Zavrsen">Završeno</option>
          <option value="Na čekanju">Na čekanju</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="poceo" class="form-label">Počeo</label>
        <input
          type="date"
          class="form-control"
          id="poceo"
          v-model="poceo"
          required
        />
      </div>

      <div class="mb-3">
        <label for="zavrsio" class="form-label">Završio</label>
        <input
          type="date"
          class="form-control"
          id="zavrsio"
          v-model="zavrsio"
        />
      </div>

      <div class="mb-3">
        <label for="progres" class="form-label">Progres (%)</label>
        <input
          type="number"
          class="form-control"
          id="progres"
          v-model="progres"
          min="0"
          max="100"
          required
        />
      </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>

<style scoped>
</style>



