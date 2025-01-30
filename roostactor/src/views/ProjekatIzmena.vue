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
const tip = ref("");
const status = ref("");  // This can be dynamically set based on form input
const poceo = ref("");
const zavrsio = ref("");
const progres = ref("");
const tim = ref("");
const opis = ref("");

// Set the current date for the "poceo" field
onMounted(() => {
  const today = new Date();
  const formattedDate = today.toISOString().split("T")[0]; // Format: YYYY-MM-DD
  poceo.value = formattedDate;

  // Fetch project data
  fetchProject();
});

// Function to fetch the project data based on the provided ID
const fetchProject = async () => {
  try {
    const response = await axios.get(`http://localhost:5000/projekti/${id}`);
    console.log(response.data);  // Log the response to check the value of 'status'
    const formatDate = (date) => date ? date.split('T')[0] : '';

    naziv.value = response.data.naziv;
    tip.value = response.data.tip;
    status.value = response.data.status;  // Ensure status is correctly assigned
    poceo.value = formatDate(response.data.poceo);
    zavrsio.value = formatDate(response.data.zavrsio);
    progres.value = response.data.progres;
    tim.value = response.data.tim;
    opis.value = response.data.opis;

    console.log("Fetched status:", status.value);  // Debugging log for status
  } catch (error) {
    toast.error(error.response?.data?.message || "Greška pri učitavanju podataka.");
  }
};



// Handle form submission
const handleSubmit = async (event) => {
  event.preventDefault();

  try {
    const response = await axios.put(`http://localhost:5000/projekat-izmena/${id}`, {
      naziv: naziv.value,
      tip: tip.value,
      status: status.value || "U toku", // Default to "U toku" if not selected
      poceo: poceo.value,
      zavrsio: zavrsio.value,
      progres: progres.value || 0,
      tim : tim.value,
      opis : opis.value
       // Default to 0 if no value is set
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
  <FormContainer title="Izmeni Projekat">
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

      <div class="mb-3">
      <label for="tim" class="form-label">Tim</label>
      <input
        type="text"
        class="form-control large-input"
        id="tim"
        v-model="tim"
        required
      />
    </div>

    <div class="mb-3">
      <label for="opis" class="form-label">Opis</label>
      <input
        type="text"
        class="form-control large-input"
        id="opis"
        v-model="opis"
        required
      />
    </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>

<style scoped>
</style>

