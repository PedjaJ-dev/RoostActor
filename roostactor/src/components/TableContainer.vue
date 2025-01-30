<script setup>
import { defineProps } from "vue";
import { RouterLink, useRoute } from "vue-router";

// Define props for passing the link, button text, and title
const props = defineProps({
  to: {
    type: String,
    required: true,
  },
  buttonText: {
    type: String,
    required: true,
  },
  Naslov: {
    type: String,
    required: true,
  }
});

// Use the `useRoute` to get current route information
const route = useRoute();

// Check if the current route is 'dashboard'
const isDashboardPage = route.name === 'dashboard';
const isProjectInfoPage = route.name === 'ProjekatInfo' && route.params.id;
const isStatistika = route.name === 'statistika';

</script>

<template>
  <!-- Display the title passed as a prop -->
  <h1>{{ Naslov }}</h1>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <!-- Row wrapping the table and button -->
    <div class="row w-100 text-center">
      <div class="col-12">
        <!-- Dynamically bind the 'table-bordered' class based on the route -->
        <table :class="{'table-bordered': !isDashboardPage}" class="table text-center mx-auto">
          <thead class="thead-dark">
            <slot name="table-header"></slot>
          </thead>
          <tbody>
            <slot name="table-body"></slot>
          </tbody>
        </table>
      </div>

      <!-- Button centered horizontally and vertically -->
      <div class="col-12 my-3" v-if="!isDashboardPage && !isProjectInfoPage && !isStatistika">
        <RouterLink :to="to" role="button" class="btn btn-primary">
          {{ buttonText }}
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.btn-primary {
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

.btn-primary:hover {
  background-color: salmon;
  text-decoration: none;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 1000px;
}

.table {
  width: 80%;
  margin-top: 20px;
  border-collapse: collapse;
}

.table th, .table td {
  padding: 10px;
  text-align: center;
  border: 1px solid #ddd;
}

.table thead {
  background-color: #f8f9fa;
  font-weight: bold;
}

h1 {
  color: red;
  position: absolute;
  top: 17%;
  left: 570px;
}
</style>







  
  
 
