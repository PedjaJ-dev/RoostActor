<script setup>
import { ref, onMounted } from "vue";
import TableContainer from "@/components/TableContainer.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const projekti = ref([]);
const projekatToDelete = ref(null);
const confirmModalRef = ref(null);
const Naslov = "Projekti";

// Provera uloge iz localStorage
const isAdmin = localStorage.getItem("rola") === "Administrator";

// Fetch the list of projects from the server
const fetchProjekti = async () => {
  try {
    const response = await axios.get("http://localhost:5000/projekti", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
    projekti.value = response.data;
  } catch (error) {
    toast.error("Greška prilikom preuzimanja projekata.");
  }
};

// Confirm project deletion
const confirmDelete = (projekat) => {
  projekatToDelete.value = projekat;
  confirmModalRef.value.showModal();
};

// Delete project
const deleteProjekat = async () => {
  try {
    await axios.delete(
      `http://localhost:5000/projekti/${projekatToDelete.value.IDP}`,
      {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      }
    );
    projekti.value = projekti.value.filter(
      (projekat) => projekat.IDP !== projekatToDelete.value.IDP
    );
    projekatToDelete.value = null;
    toast.success("Projekat uspešno obrisan.");
  } catch (error) {
    toast.error("Greška prilikom brisanja projekta.");
  }
};

// Navigate to edit project page
const navigateToEdit = (projekatId) => {
  if (projekatId) {
    router.push({ path: `/projekat-izmena/${projekatId}` });
  }
};

const navigateToSee = (projekatId) => {
  if (projekatId) {
    router.push({ path: `/projekat-info/${projekatId}` });
  }
};

onMounted(fetchProjekti);
</script>

<template>
  <div class="center-container">
    <!-- Pass props to TableContainer component including the title -->
    <TableContainer :Naslov="Naslov" to="/projekat-novi" buttonText="Dodaj projekat">
      <!-- Define the table header slot -->
      <template #table-header>
        <tr>
          <th scope="col">Naziv</th>
          <th scope="col">Tip</th>
          <th scope="col">Status</th>
          <th scope="col">Počeo</th>
          <th scope="col">Završio</th>
          <th scope="col">Progres</th>
          <th scope="col">Akcije</th> <!-- Added column for action buttons -->
        </tr>
      </template>

      <!-- Define the table body slot -->
      <template #table-body>
        <tr v-for="projekat in projekti" :key="projekat.IDP">
          <td>{{ projekat.naziv }}</td>
          <td>{{ projekat.tip }}</td>
          <td>{{ projekat.status }}</td>
          <td>{{ projekat.poceo }}</td>
          <td>{{ projekat.zavrsio }}</td>
          <td>{{ projekat.progres }}</td>
          <td class="actions">
            <button @click="navigateToEdit(projekat.IDP)"><img src="/src/assets/img/edit.png" alt="edit" /></button>
            <!-- Prikazivanje dugmeta za brisanje samo ako je korisnik Administrator -->
            <button 
              v-if="isAdmin"
              @click="confirmDelete(projekat)"
              class="text-danger mx-1 btn btn-link"
            >
              <img src="/src/assets/img/delete.png" alt="delete" />
            </button>
            <button @click="navigateToSee(projekat.IDP)"><img src="/src/assets/img/info.png" alt="info"/></button>
          </td>
        </tr>
      </template>
    </TableContainer>

    <!-- Delete Confirmation Modal -->
    <DeleteModal 
      ref="confirmModalRef" 
      :title="'Potvrda brisanja'" 
      :message="'Da li ste sigurni da želite da obrišete projekat?'" 
      :onConfirm="deleteProjekat" 
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
  width: 400px;
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



