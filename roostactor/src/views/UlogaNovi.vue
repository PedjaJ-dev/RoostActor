<script setup>
import { ref } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import { useRouter } from "vue-router";
import FormContainer from "@/components/FormContainer.vue";

const router = useRouter();

const ime = ref("");
const prezime = ref("");
const uloga = ref("");

const handleSubmit = async (event) => {
  event.preventDefault();
  try {
    const response = await axios.post("/api/projekat-novi", {
      ime: ime.value,
      prezime: prezime.value,
      uloga: uloga.value,
    });
    router.push("/projekti").then(() =>
      toast.success(response.data.message)
    );
  } catch (error) {
    toast.error(error.response.data.message || error.message);
  }
};
</script>

<template>
  <FormContainer title="Nova Uloga">
    <form @submit="handleSubmit">
      <div class="mb-3">
        <label for="ime" class="form-label">Ime</label>
        <input
          type="text"
          class="form-control"
          id="ime"
          v-model="ime"
          required
        />
      </div>

      <div class="mb-3">
        <label for="prezime" class="form-label">Prezime</label>
        <input
          type="text"
          class="form-control"
          id="prezime"
          v-model="prezime"
          required
        />
      </div>

      <div class="mb-3">
        <label for="uloga" class="form-label">Uloga</label>
        <input
          type="text"
          class="form-control"
          id="uloga"
          v-model="uloga"
          required
        />
      </div>

      <button type="submit" class="btn btn-primary">Sačuvaj</button>
    </form>
  </FormContainer>
</template>

<style scoped>
</style>
