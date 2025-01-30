<script setup>
import { RouterLink, useRoute } from "vue-router"; 
import { useRouter } from "vue-router"; 
import { useUserRole } from "@/composables/useUserRole.js"; 
import { toast } from "vue3-toastify"; 
import axios from "axios"; 
import { onMounted } from "vue"; 

const router = useRouter(); 
const { userRole, checkUserRole } = useUserRole(); 

// Definisanje userId, token-a i role iz localStorage
const accessToken = localStorage.getItem("access_token");
const userId = localStorage.getItem("userId");
const rola = localStorage.getItem("rola");

// Provera da li korisnik ima pristup
onMounted(() => {
  if (!accessToken) {
    toast.error("Niste ulogovani.");
    router.push("/login"); // Ako korisnik nije ulogovan, preusmerava ga na login stranicu
  } else {
    checkUserRole(); // Provera korisničke uloge ako je korisnik ulogovan
  }
});

const isActiveLink = (routePath) => {
  const route = useRoute();
  return route.path === routePath; 
}; 

const handleLogout = async () => { 
  try { 
    localStorage.removeItem("access_token"); 
    localStorage.removeItem("userId"); // Uklanjamo userId iz localStorage prilikom logout-a
    localStorage.removeItem("rola"); // Uklanjamo rolu
    router.push("/login").then(()  =>  toast.success("Uspešno ste se odjavili.")); 
  } catch (error) { 
    toast.error(error.response?.data?.message || error.message); 
  } 
}; 
</script> 

<template> 
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary"> 
    <div class="container-fluid"> 
      <img src="/src/assets/img/logo.png"/>
    </div> 
  </nav> 
   <br><br><br>
  <ul class="nav flex-column">
    <br>
    <li class="nav-item">
      <div class="nav-content">
        <img src="/src/assets/img/dashboard.png" alt="Logo" class="logo"/>
        <a class="nav-link" :href="`/dashboard/${userId}`">Dashboard</a>
      </div>

      <div class="nav-content">
        <img src="/src/assets/img/user.png" alt="Logo" class="logo"/>
        <a class="nav-link" href="/korisnici">Korisnici</a>
      </div>

      <div class="nav-content">
        <img src="/src/assets/img/project.png" alt="Logo" class="logo"/>
        <a class="nav-link" href="/projekti">Projekti</a>
      </div>

      <div class="nav-content">
        <img src="/src/assets/img/fire.png" alt="Logo" class="logo"/>
        <a class="nav-link" href="/statistika">Popularnost projekta</a>
      </div>

      <br><br><br><br><br><br><br><br><br><br>
      <div class="nav-content">
        <img src="/src/assets/img/logout.png" alt="Logo" class="logo"/>
        <a class="nav-link" @click.prevent="handleLogout">Logout</a>
      </div>

    </li>
  </ul>
</template>

<style scoped>
nav{
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
}

img{
  width: 65px;
  height: 65px;
}

.navbar.bg-primary {
  background-color: #f26050 !important;
}

#naslov{
  position: relative;
  top: 5px;
  right: 86%;
  color: white;
  font-style: very-bold;
  font-size: 20px;
}

.nav {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 200px;
  height: 86.3%;
  background-color: white;
  border-right: 1px solid grey;
  overflow: hidden;
}

.nav-link{
  color: #94190d;
}

.nav-content {
  display: flex;
  align-items: center;
}

.logo {
  width: 30px;
  height: auto;
  margin-right: 10px;
}

@media (max-width: 1024px) {
  #naslov{
    position: relative;
    top: 5px;
    right: 59%;
    color: white;
    font-style: very-bold;
    font-size: 20px;
  }
}
</style>
