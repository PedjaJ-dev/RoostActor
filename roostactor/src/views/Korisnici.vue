<script setup>
import { ref, onMounted } from "vue";
import TableContainer from "@/components/TableContainer.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const korisnici = ref([]);
const korisnikToDelete = ref(null);
const confirmModalRef = ref(null);
const Naslov = "Korisnici";
const { id } = defineProps();

// Provera uloge iz localStorage
const isAdmin = localStorage.getItem("rola") === "Administrator";

const fetchKorisnici = async () => {
  try {
    const response = await axios.get("http://localhost:5000/korisnici", {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
    korisnici.value = response.data;
  } catch (error) {
    toast.error("Greška prilikom preuzimanja korisnika.");
  }
};

const confirmDelete = (korisnik) => {
  korisnikToDelete.value = korisnik;
  confirmModalRef.value.showModal();
};

const deleteKorisnik = async () => {
  try {
    await axios.delete(
      `http://localhost:5000/korisnici/${korisnikToDelete.value.IDK}`,
      {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      }
    );
    korisnici.value = korisnici.value.filter(
      (k) => k.IDK !== korisnikToDelete.value.IDK
    );
    korisnikToDelete.value = null;
    toast.success("Korisnik uspešno obrisan.");
  } catch (error) {
    toast.error("Greška prilikom brisanja korisnika.");
  }
};

const navigateToEdit = (korisnikId) => {
  if (korisnikId) {
    router.push({ name: 'KorisnikIzmena', params: { id: korisnikId } });
  }
};

onMounted(fetchKorisnici);
</script>

<template>
  <div class="center-container">
    <!-- Pass props to TableContainer component including the title -->
    <TableContainer
      :Naslov="Naslov"
      to="/korisnik-novi"
      buttonText="Dodaj korisnika"
    >
      <template #table-header>
        <tr>
          <th scope="col">Ime</th>
          <th scope="col">Prezime</th>
          <th scope="col">Email</th>
          <th scope="col">Rola</th>
          <th scope="col">Akcije</th>
        </tr>
      </template>

      <!-- Define the table body slot -->
      <template #table-body>
        <tr v-for="korisnik in korisnici" :key="korisnik.IDK">
          <td>{{ korisnik.Ime }}</td>
          <td>{{ korisnik.Prezime }}</td>
          <td>{{ korisnik.Email }}</td>
          <td>{{ korisnik.Uloga }}</td>
          <td class="actions">
            <button @click="navigateToEdit(korisnik.IDK)">
              <img src="/src/assets/img/edit.png" alt="edit" />
            </button>
            <!-- Prikazivanje dugmeta za brisanje samo ako je korisnik Administrator -->
            <button
              v-if="isAdmin"
              @click="confirmDelete(korisnik)"
              class="text-danger mx-1 btn btn-link"
            >
              <img src="/src/assets/img/delete.png" alt="delete" />
            </button>
          </td>
        </tr>
      </template>
    </TableContainer>
  </div>

  <DeleteModal
    ref="confirmModalRef"
    :title="'Potvrda brisanja'"
    :message="'Da li ste sigurni da želite da obrišete korisnika?'"
    :onConfirm="deleteKorisnik"
  />
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

