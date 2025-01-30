<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from "./components/Navbar.vue";
import { toast } from "vue3-toastify"; 
</script>

<template>
  <div>
    <Navbar v-if="$route.name !== 'Login' &&
                $route.name !== 'korisnik-novi' &&
                $route.name !== 'projekat-novi' &&
                $route.name !== 'uloga-novi' &&
                !$route.path.startsWith('/korisnik-izmena') &&
                !$route.path.startsWith('/projekat-izmena') &&
                !$route.path.startsWith('/info-izmena')&&
                !$route.path.startsWith('/statistika-izmena')">
</Navbar>

    <RouterView></RouterView>
  </div>
</template>




