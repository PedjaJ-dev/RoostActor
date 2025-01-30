<script setup>
import { ref } from "vue";
import TableContainer from "/src/components/TableContainer.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import { toast } from "vue3-toastify"; 
import "vue3-toastify/dist/index.css"; 
import axios from "axios";

// Define sample data for "uloge"
const uloge = ref([
  { id: 1, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
  { id: 2, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
  { id: 3, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
  { id: 4, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
  { id: 5, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
  { id: 6, ime: "Web Development", prezime: "Frontend", uloga: "In Progress" },
]);

const ulogaToDelete = ref(null); 
const confirmModalRef = ref(null); 

// Corrected function name here
const confirmDelete = (uloga) => { 
  ulogaToDelete.value = uloga; 
  confirmModalRef.value.showModal(); 
};

// Fixed variable name to match the one in script setup
const deleteUloga = () => {
  try {
    // Remove the user from the list
    uloge.value = uloge.value.filter(uloga => uloga.id !== ulogaToDelete.value.id);

    // Clear the reference to the deleted user
    ulogaToDelete.value = null;

    // Show success toast
    toast.success("Uloga uspešno obrisana");

  } catch (error) {
    // Handle any errors (although there shouldn't be any in this case)
    toast.error("Greška prilikom brisanja uloge.");
  }
};


const Naslov = "Uloge";
</script>

<template>
  <div class="center-container">
    <!-- Pass props to TableContainer component including the title -->
    <TableContainer :Naslov="Naslov" to="/uloga-novi" buttonText="Dodaj ulogu">
      <!-- Define the table header slot -->
      <template #table-header>
        <tr>
          <th scope="col">Ime</th>
          <th scope="col">Prezime</th>
          <th scope="col">Uloga</th>
          <th scope="col">Akcije</th>
        </tr>
      </template>

      <!-- Define the table body slot -->
      <template #table-body>
        <tr v-for="uloga in uloge" :key="uloga.id">
          <td>{{ uloga.ime }}</td>
          <td>{{ uloga.prezime }}</td>
          <td>{{ uloga.uloga }}</td>
          <td class="actions">
            <button><img src="/src/assets/img/edit.png" alt="edit"/></button>
            <button @click="confirmDelete(uloga)"><img src="/src/assets/img/delete.png" alt="delete"/></button>
          </td>
        </tr>
      </template>
    </TableContainer>

    <!-- Delete Modal -->
    <DeleteModal 
      ref="confirmModalRef" 
      :title="'Potvrda brisanja'" 
      :message="'Da li ste sigurni da želite da obrišete ulogu?'" 
      :onConfirm="deleteUloga" 
    />
  </div>
</template>

<style scoped>
.center-container {
  display: flex;
  justify-content: flex-start; 
  align-items: center;
  max-height: 100vh;
  flex-direction: column;
  width: 100%;
  padding-left: 14%;
  padding-top: 5%;
}

.table {
  width: 80%;
  border-collapse: collapse;
}

.table th, .table td {
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
</style>
