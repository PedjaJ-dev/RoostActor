import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Vue3Toastify from 'vue3-toastify'
import "/node_modules/vue3-toastify/dist/index.css"
import router from './router'
import axios from 'axios'

const app = createApp(App)

app.use(Vue3Toastify,{
    autoClose:3000,
})


setInterval(() => {
    localStorage.clear();
    }, 30 * 60 * 1000);

axios.interceptors.request.use(
(config) => {
const token = localStorage.getItem("access_token");
if (token) {
config.headers.Authorization = `Bearer ${token}`;
}
return config;
},
(error) => {
return Promise.reject(error);
}
);

app.use(router)

app.mount('#app')
