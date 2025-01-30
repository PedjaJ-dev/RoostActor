<template>
  <div class="form-container">
    <h1>{{ title }}</h1>
    <slot></slot> <!-- Ovo omogućava da se sadržaj iz forme ubaci ovde -->
  </div>
</template>

<script setup>
defineProps(['title']); // Ova linija omogućava da prosleđuješ `title` kao prop
</script>

<style scoped>
.form-container {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  position: absolute;
  top: 35px; /* Pozicionirajte ga na željenu udaljenost od vrha */
  right: 400px; /* Pozicionirajte ga na desnu ivicu */
}
</style>





