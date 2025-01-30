<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import TableContainer from "@/components/TableContainer.vue";

// Reactive variables for user data
const ime = ref('');
const prezime = ref('');
const uloga = ref('');
const email = ref('');

// Retrieve userId from localStorage
const userId = localStorage.getItem('userId');

// Fetch user data from API
const fetchUserData = async () => {
  if (!userId) {
    toast.error("Nema logovanog korisnika.");
    return;
  }

  try {
    const response = await axios.get(`http://localhost:5000/korisnici/${userId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    });

    const data = response.data;
    ime.value = data.ime;
    prezime.value = data.prezime;
    email.value = data.email;
    uloga.value = data.uloga;
  } catch (error) {
    toast.error("Došlo je do greške prilikom učitavanja podataka!");
  }
};

onMounted(() => {
  fetchUserData();
});
</script>

<template>
  <div class="center-container">
    <TableContainer :Naslov="`Welcome, ${ime} ${prezime}`">
      <template #table-header>
        <tr>
          <td class="right-align">Ime</td>
          <td>{{ ime }}</td>
        </tr>
        <tr>
          <td class="right-align">Prezime</td>
          <td>{{ prezime }}</td>
        </tr>
        <tr>
          <td class="right-align">Uloga</td>
          <td>{{ uloga }}</td>
        </tr>
        <tr>
          <td class="right-align">Email</td>
          <td>{{ email }}</td>
        </tr>
      </template>
    </TableContainer>
  </div>
</template>

<style scoped>
/* Stilizacija tvoje komponente */
.center-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  max-height: 100vh;
  flex-direction: column;
  width: 124%;
  padding-left: 14%;
  padding-top: 5%;
}

table {
  position: relative;
  left: 150%;
  top: 6%;
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  text-align: left;
}

th img {
  max-width: 50px;
}

button {
  background-color: red;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  border-radius: 5px;
  display: inline-block;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: salmon;
  text-decoration: none;
}

.right-align {
  text-align: right;
  justify-content: right;
}
</style>





  






