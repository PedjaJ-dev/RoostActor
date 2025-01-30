<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { toast } from "vue3-toastify";

const email = ref("");
const lozinka = ref("");
const router = useRouter();

// Uzimanje tokena, userId i role iz localStorage-a pri učitavanju stranice
const accessToken = ref(localStorage.getItem("access_token"));
const userId = ref(localStorage.getItem("userId"));
const rola = ref(localStorage.getItem("rola"));

// Provera da li je korisnik već ulogovan
onMounted(() => {
  if (accessToken.value) {
    // Ako je korisnik već ulogovan, preusmeriti ga na njegov dashboard
    router.push(`/dashboard/${userId.value}`);
  }
});

const handleSubmit = async (event) => {
  event.preventDefault();

  // Validacija da email i lozinka nisu prazni
  if (!email.value || !lozinka.value) {
    toast.error("Molimo vas da popunite sva polja.");
    return;
  }

  try {
    const response = await axios.post("http://localhost:5000/login", {
      email: email.value,
      lozinka: lozinka.value,
    });

    // Spremanje tokena, userId i uloge u localStorage
    localStorage.setItem("access_token", response.data.access_token);
    localStorage.setItem("userId", response.data.userId);
    localStorage.setItem("rola", response.data.uloga);

    // Preusmeravanje na dashboard korisnika
    router.push(`/dashboard/${response.data.userId}`).then(() => {
      toast.success(response.data.message);
    });
  } catch (error) {
    toast.error(error.response?.data?.message || error.message);
  }
};
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-6 col-xs-12">
        <form @submit="handleSubmit">
          <div class="form-group mb-3">
            <label>Email adresa</label>
            <input type="email" v-model="email" class="form-control" required />
          </div>
          <div class="form-group mb-3">
            <label>Lozinka</label>
            <input
              type="password"
              v-model="lozinka"
              class="form-control"
              required
            />
          </div>
          <input
            type="submit"
            class="btn btn-primary"
            role="button"
            value="Prijavi se"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: salmon;
  width: 40vw; /* 50% of the viewport width */
  height: 50vh; /* 50% of the viewport height */
  margin: 50vh;
  padding-top: 4vw;
  border-radius: 10%;
}

label {
  color: red;
  font-size: 20px;
}

.btn {
  background-color: red;
  color: white;
  border: red;
  width: 100%;
  font-size: 20px;
}
</style>


