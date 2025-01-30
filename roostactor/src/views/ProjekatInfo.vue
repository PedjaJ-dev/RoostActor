<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import TableContainer from "@/components/TableContainer.vue";
import { useRoute } from "vue-router"; // Uvoz useRoute iz Vue Router-a

// Inicijalizuj reactive varijable
const naziv = ref("");
const opis = ref("");
const tim = ref("");
const id = ref(null);

// Uzmi projekatId iz parametara rute
const route = useRoute();
const projekatId = ref(route.params.id); // Uzmi projekatId sa rute

// Funkcija za preuzimanje podataka o projektu
const fetchProjekatData = async () => {
  try {
    const response = await axios.get(`http://localhost:5000/projekat-info/${projekatId.value}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    });

    const data = response.data;
    naziv.value = data.naziv;
    opis.value = data.opis;
    tim.value = data.tim;
  } catch (error) {
    toast.error("Došlo je do greške prilikom učitavanja podataka!");
  }
};

// Pozovi funkciju za preuzimanje podataka kad se komponenta montira
onMounted(() => {
  fetchProjekatData();
  const route = useRoute();
  id.value = route.params.id;
  console.log(id.value);
});
</script>

<template>
  <div class="center-container">
    <TableContainer :Naslov="naziv" :to="'/info-izmena/' + id" buttonText="Izmeni">
      <template #table-header>
        <tr>
          <td class="right-align" style="width: 15%">Opis</td>
          <td>{{ opis }}</td>
        </tr>
        <tr>
          <td class="right-align">Tim</td>
          <td>{{ tim }}</td>
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
  max-height: 117vh;
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


#edit{
    background-color: darksalmon;
}
</style>



  
  