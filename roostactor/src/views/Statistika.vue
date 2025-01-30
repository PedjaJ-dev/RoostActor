<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import TableContainer from "@/components/TableContainer.vue";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import axios from "axios";

const router = useRouter();
const route = useRoute();  // Access route parameters
const projekti = ref([]);
const Naslov = "Popularnost projekta";

// Fetch the list of projects from the server
const fetchProjekti = async () => {
  try {
    const response = await axios.get("http://localhost:5000/statistika", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
    console.log("API Response:", response);
    projekti.value = response.data;
  } catch (error) {
    console.error("API Error:", error);
    toast.error("Greška prilikom preuzimanja podataka.");
  }
};

// Navigate to edit project page using projekatId from route params
const navigateToEdit = (projekatId) => {
  console.log("Navigating to edit with ID:", projekatId); // Debug log for the ID
  if (projekatId) {
    router.push({ path: `/statistika-izmena/${projekatId}` });
  } else {
    toast.error("ID projekta nije validan.");
  }
};

// Navigate to project info page using projekatId from route params
const navigateToSee = (projekatId) => {
  if (projekatId) {
    router.push({ path: `/statistika-info/${projekatId}` });
  }
};

onMounted(fetchProjekti);
</script>

<template>
  <div class="center-container">
    <!-- Pass props to TableContainer component including the title -->
    <TableContainer :Naslov="Naslov" to="/statistika-novi" buttonText="Dodaj projekat">
      <!-- Define the table header slot -->
      <template #table-header>
        <tr>
          <th scope="col">Naziv</th>
          <th scope="col">Gledanost</th>
          <th scope="col">Prihodi</th>
          <th scope="col">Ocena</th>
        </tr>
      </template>

      <!-- Define the table body slot -->
      <template #table-body>
        <tr v-for="projekat in projekti" :key="projekat.IDP">
          <td>{{ projekat.Naziv }}</td>
          <td>{{ projekat.Gledanost }}</td>
          <td>{{ projekat.Prihodi }}</td>
          <td>{{ projekat.Ocena }}</td>
        </tr>
      </template>
    </TableContainer>
  </div>
</template>

<style scoped>
.center-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  max-height: 200%;
  flex-direction: column;
  width: 100%;
  padding-left: 14%;
  padding-top: 5%;
}

.table {
  width: 80%;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: 5px 8px;
  text-align: center;
  border: 1px solid #ddd;
  height: 30px;
}

.table thead {
  background-color: #f8f9fa;
  font-weight: bold;
}

.actions button {
  margin: 0 5px;
}

button {
  border: white;
  background-color: white;
}

img {
  width: 20px;
}

.input-group {
  width: 400px;
  background-color: white;
  height: 40px;
}

.btn-primary {
  background-color: greenyellow;
  height: 40px;
}

#form1 {
  border: 1px solid black;
  width: 200%;
}
</style>



